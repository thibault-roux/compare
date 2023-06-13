from utils.io import read, intersect
import pickle

def getdata():
    # check if pickle exists
    try:
        with open("pickle/localise.pkl", "rb") as file:
            chardata, bpe1000data, bpe750data = pickle.load(file)
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

        # save pickle
        with open("pickle/localise.pkl", "wb") as file:
            pickle.dump((chardata, bpe1000data, bpe750data), file)

    return chardata, bpe1000data, bpe750data



if __name__ == "__main__":
    chardata, bpe1000data, bpe750data = getdata()

    