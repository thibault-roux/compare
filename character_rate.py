from utils.leven import levenstein_alignment


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
    data = read(filename)

    occ = dict()
    err = dict()

    for id, refhyp in data.items():
        ref = refhyp[0]
        hyp = refhyp[1]
        ref, hyp, binary_list = levenstein_alignment(ref, hyp)
        for r, b in zip(ref, hyp):
            if r not in occ:
                occ[r] = 0
            occ[r] += 1
            if r != b:
                if r not in err:
                    err[r] = 0
                err[r] += 1

    for k, v in occ.items():
        print(k, v, err[k])

if __name__ == "__main__":
    filename1 = "KD_woR"
    filename2 = "KD_wR"

    character_rate(filename1)
    # long à calculer, vérifier pourquoi ?