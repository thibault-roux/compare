from utils.io import read, intersect
import pickle
from jiwer import cer

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



if __name__ == "__main__":
    data = getdata()

    # now we loaded the data, we can plot lines of CER for each sentence
    cer_dict = dict()
    cer_dict["char"] = []
    cer_dict["bpe1000"] = []
    cer_dict["bpe750"] = []
    for id, refhyp in chardata.items():
        pass

    