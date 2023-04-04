import pickle

def voc(csvfile):
    voc = set()
    with open(csvfile, "r") as f:
        for line in f:
            line = line.lower()
            voc.update(line.split(",")[3].split())
    return voc

if __name__ == "__main__":
    words = voc(csvfile="mytest.csv") - voc(csvfile="ALL.csv") # words in test set but not in training set
    print(len(words)) # less than 1% of vocabulary of test set

    #print(words)
    todelete = set()
    for word in words:
        for c in word:
            if c not in "éèêçâàîïôùûabcdefghijklmnopqrstuvwxyz0123456789'":
                todelete.add(word)

    for word in todelete:
        words.remove(word)

    print(words)
    print(len(words))

    with open("words.pkl", "wb") as f:
        pickle.dump(words, f)