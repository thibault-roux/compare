import pickle
from utils.leven import levenstein_alignment
import progressbar


def read(filename):
    data = dict()
    with open("../../metrics/hypereval/data/" + filename + "/" + filename + "1.txt", "r", encoding="utf8") as file:
        for line in file:
            line = line.split("\t")
            id = line[0]
            ref = line[1]
            hyp = line[2]
            data[id] = [ref, hyp]
    return data

def character_rate(filename):
    print("Reading data...")
    data = read(filename)
    print("Data read")

    occ = dict()
    err = dict()

    print("Computing...")
    bar = progressbar.ProgressBar(max_value=len(data))
    i = 0
    for id, refhyp in data.items():
        i += 1
        bar.update(i)
        ref = refhyp[0]
        hyp = refhyp[1]
        ref, hyp, binary_list = levenstein_alignment(ref, hyp) # this call takes some time applied on character
        for r, b in zip(ref, hyp):
            if r not in occ:
                occ[r] = 0
            occ[r] += 1
            if r != b:
                if r not in err:
                    err[r] = 0
                err[r] += 1
    print("End of computation")

    for k, v in occ.items():
        try:
            print(k, v, err[k]) # keyError: '7'
        except KeyError:
            print(k, v, 0, "KeyError")


    # store in a pickle file the occ
    with open("pickle/" + filename + "_occ.pkl", "wb") as file:
        pickle.dump(occ, file)
    
    # store in a pickle file the err
    with open("pickle/" + filename + "_err.pkl", "wb") as file:
        pickle.dump(err, file)


def check(filename):
    with open("pickle/" + filename + "_occ.pkl", "rb") as file:
        occ = pickle.load(file)
    for k, v in occ.items():
        print(k, v)

if __name__ == "__main__":
    # filename1 = "KD_woR"
    # filename2 = "KD_wR"

    character_rate("SB_w2v_7k")
    character_rate("SB_bpe250")
    character_rate("SB_bpe500")
    character_rate("SB_bpe750")
    character_rate("SB_bpe1000")