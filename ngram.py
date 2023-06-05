from utils.io import read, intersect


def train_ngram(corpus, n):
    probs = dict()
    occ = dict()
    for ligne in corpus:
        for i in range(len(ligne)-2):
            c1 = ligne[i]
            c2 = ligne[i+1]
            if c1 in occ:
                occ[c1] += 1
            else:
                occ[c1] = 1
            if c1 not in probs:
                probs[c1] = dict()
                probs[c1][c2] = 1
            else:
                if c2 not in probs[c1]:
                    probs[c1][c2] = 1
                else:
                    probs[c1][c2] += 1
    return probs, occ

def compute_probability(sentence, probs, n, occ): # probs is a dict of probabilities of a n-gram, n is the length of a ngram
    probabilities = [] # list of probabilities of each n-gram
    if len(sentence) < n:
        return 0
    for i in range(len(sentence)-1):
        if i < len(sentence)-1: # -n+1 ?
            c1 = sentence[i]
            c2 = sentence[i+1]
            try:
                proba = probs[c1][c2]/occ[c1]
            except KeyError:
                proba = 0
            probabilities.append(proba)
    try:
        retour = sum(probabilities)/len(probabilities)
    except ZeroDivisionError:
        print("sentence:", sentence)
        print("probabilities:", probabilities)
        raise
    return retour

if __name__ == "__main__":
    filename1 = "SB_bpe750" # bpe 750
    name1 = "bpe 750"
    filename2 = "SB_w2v_7k" # char
    name2 = "char"
    data1 = read(filename1)
    data2 = read(filename2)
    data1, data2 = intersect(data1, data2)

    print("Loading data...")
    """# get references
    refs = []
    for id, refhyp in data1.items():
        refs.append(refhyp[0])"""
    with open("/users/troux/these/expe/end-to-end/asr_model/LM/data/train.txt", "r", encoding="utf8") as file:
        data_train = []
        for ligne in file:
            data_train.append(ligne[:-1].lower())
    
    print("Training ngram...")
    n = 1
    probs, occ = train_ngram(data_train, n)
    # compteur
    hyp1_better = 0
    hyp2_better = 0
    equal = 0

    for id, refhyp in data1.items():
        if id not in data2:
            raise Exception("ids are not the same. Check first column of data.")
        if refhyp[0] != data2[id][0]:
            raise Exception("ids are not the same. Check first column of data.")

        # compute probability
        sentence = refhyp[1]
        probability1 = compute_probability(sentence, probs, n, occ)
        sentence = data2[id][1]
        probability2 = compute_probability(sentence, probs, n, occ)

        # update counter
        if probability1 < probability2:
            hyp1_better += 1
        elif probability1 > probability2:
            hyp2_better += 1
        else:
            equal += 1

    print(name1, "better: ", hyp1_better)
    print(name2, "better: ", hyp2_better)
    print("equal: ", equal)