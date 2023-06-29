from utils.io import read, intersect



def compute_perplexity(sentence, tokenizer, model):
    # Tokenize the input sentence
    inputs = tokenizer.encode(sentence, return_tensors='pt')

    # Generate predictions from the model
    with torch.no_grad():
        outputs = model(inputs, labels=inputs)
        loss = outputs.loss

    # Calculate perplexity
    perplexity = torch.exp(loss)

    print()
    print(perplexities)
    input()

    return perplexity.item()

def evaluate(filename1, filename2, name1, name2, words=False):
    data1 = read(filename1)
    data2 = read(filename2)
    data1, data2 = intersect(data1, data2)

    
    # compteur
    hyp1_more_probable = 0
    hyp2_more_probable = 0
    equal = 0

    for id, refhyp in data1.items():
        if id not in data2:
            raise Exception("ids are not the same. Check first column of data.")
        if refhyp[0] != data2[id][0]:
            raise Exception("ids are not the same. Check first column of data.")
        if refhyp[1] == data2[id][1]:
            continue

        # compute probability
        sentence = refhyp[1]
        probability1 = compute_probability(sentence, probs, n, occ, words=words)
        sentence = data2[id][1]
        probability2 = compute_probability(sentence, probs, n, occ, words=words)
        if probability1 < 0 or probability2 < 0 or probability1 > 1 or probability2 > 1:
            raise Exception("probability is not between 0 and 1")
        # print(probability1 - probability2)

        # update counter
        if probability1 > probability2:
            hyp1_more_probable += 1
        elif probability1 < probability2:
            hyp2_more_probable += 1
        else:
            equal += 1

    print(name1, "more probable: ", hyp1_more_probable)
    print(name2, "more probable: ", hyp2_more_probable)
    print("equal: ", equal)


if __name__ == "__main__":
    # in the future, compute different probabilities with different n-grams values



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
    sentence1 = "salut tu vas bien"
    probability1 = compute_probability(sentence1, probs, n, occ)
    sentence2 = "saldt uu vadqiffn"
    probability2 = compute_probability(sentence2, probs, n, occ)
    print(sentence1, probability1)
    print(sentence2, probability2)



    exit(-1)



    words = True # if True, compute probabilities with words, else with characters

    filename1 = "SB_bpe1000" # bpe 1000
    name1 = "bpe 1000"
    filename2 = "SB_w2v_7k" # char
    name2 = "char"
    evaluate(filename1, filename2, name1, name2, words=words)
    print("---------------------")

    exit(-1)


    filename1 = "SB_bpe750" # bpe 750
    name1 = "bpe 750"
    filename2 = "SB_w2v_7k" # char
    name2 = "char"
    evaluate(filename1, filename2, name1, name2, words=words)
    print("---------------------")

    filename1 = "SB_bpe1000" # bpe 1000
    name1 = "bpe 1000"
    filename2 = "SB_bpe750" # bpe 750
    name2 = "bpe 750"
    evaluate(filename1, filename2, name1, name2, words=words)
    print("---------------------")
