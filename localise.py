from utils.io import read, intersect
import pickle
from jiwer import cer
import matplotlib.pyplot as plt
import numpy as np

def getdata():
    # check if pickle exists
    try:
        with open("pickle/localise.pkl", "rb") as file:
            data = pickle.load(file)
            return chardata, bpe1000data, bpe750data
    except:    
        charfile = "SB_w2v_7k"
        bpe1000file = "SB_bpe1000"
        bpe750file = "SB_bpe750"

        chardata = read(charfile)
        bpe1000data = read(bpe1000file)
        bpe750data = read(bpe750file)

        # I need to load the data and plot if systems do errors to the same audio

        chardata, bpe1000data = intersect(chardata, bpe1000data)
        chardata, bpe750data = intersect(chardata, bpe750data)
        bpe1000data, bpe750data = intersect(bpe1000data, bpe750data)

        data = dict()
        data["char"] = chardata
        data["bpe1000"] = bpe1000data
        data["bpe750"] = bpe750data

        # save pickle
        with open("pickle/localise.pkl", "wb") as file:
            pickle.dump(data, file)

    return data


def old():
    data = getdata()

    # now we loaded the data, we can plot lines of CER for each sentence
    cer_dict = dict()
    cer_dict["char"] = []
    cer_dict["bpe1000"] = []
    cer_dict["bpe750"] = []
    cer_dict["difference"] = [] # difference between char and bpe1000
    for id, refhyp in data["char"].items():
        cer_dict["char"].append(cer(data["char"][id][0], data["char"][id][1]))
        cer_dict["bpe1000"].append(cer(data["bpe1000"][id][0], data["bpe1000"][id][1]))
        cer_dict["bpe750"].append(cer(data["bpe750"][id][0], data["bpe750"][id][1]))
        cer_dict["difference"].append(np.abs(cer_dict["char"][-1] - cer_dict["bpe1000"][-1]))


    """# Not humanly checked
    # sort by difference
    sorted_cer_dict = dict()
    sorted_cer_dict["char"] = []
    sorted_cer_dict["bpe1000"] = []
    sorted_cer_dict["bpe750"] = []
    sorted_cer_dict["difference"] = []
    sorted_cer_dict["id"] = []
    for i, diff in enumerate(sorted(cer_dict["difference"])): # sort by difference
        sorted_cer_dict["char"].append(cer_dict["char"][i])
        sorted_cer_dict["bpe1000"].append(cer_dict["bpe1000"][i])
        sorted_cer_dict["bpe750"].append(cer_dict["bpe750"][i])
        sorted_cer_dict["difference"].append(cer_dict["difference"][i])
        sorted_cer_dict["id"].append(i)"""

    for i in range(len(cer_dict["difference"])):
        if cer_dict["difference"][i] < 0: # to continue
            pass

    # plot
    plt.style.use('seaborn-whitegrid')
    step = 120
    start = 1
    y = np.arange(0, len(cer_dict["char"]), step)
    plt.scatter(y, cer_dict["char"][start::step], s=20, label="char")
    plt.scatter(y, cer_dict["bpe1000"][start::step], s=20, label="bpe1000")
    plt.scatter(y, cer_dict["bpe750"][start::step], s=20, label="bpe750")
    plt.scatter(y, cer_dict["difference"][start::step], s=20, label="difference")
    plt.legend()
    plt.show()

    plt.savefig("results/localise.png")


    # future work are the following
    # 1) plot the difference between char and bpe1000 sorted by the difference
    # 2) print sentences produced by char that are way better than bpe1000
    # and print sentences produced by bpe1000 that are way better than char



def print_different():
    data = getdata()

    name1 = "char"
    name2 = "bpe1000"

    differences = []
    for id, refhyp in data[name1].items():
        differences.append(cer(data["char"][id][1], data["char"][id][1]))


    
if __name__ == "__main__":
    print_different()