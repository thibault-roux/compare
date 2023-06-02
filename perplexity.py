import progressbar
import pickle
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

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

    return perplexity.item()


    

if __name__ == '__main__':
    # Load the tokenizer and model
    model_name = "asi/gpt-fr-cased-small"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    sent2perplexity = dict()

    filename1 = "SB_bpe1000"
    filename2 = "SB_w2v_7k"
    data1 = read(filename1)
    data2 = read(filename2)
    data1, data2 = intersect(data1, data2)

    # compteur
    hyp1_better = 0
    hyp2_better = 0
    equal = 0

    # progressbar
    bar = progressbar.ProgressBar(maxval=len(data1))
    iterator_bar = 0
    
    for id, refhyp in data1.items():
        bar.update(iterator_bar)
        iterator_bar += 1
        if id not in data2:
            raise Exception("ids are not the same. Check first column of data.")
        if refhyp[0] != data2[id][0]:
            raise Exception("refs are not the same. Check second column of data.")
        ref = refhyp[0]
        hyp1_text = refhyp[1]
        hyp2_text = data2[id][1]

        # compute perplexity
        perplexities = dict()
        for label, sent in {"ref": ref, "hyp1": hyp1_text, "hyp2": hyp2_text}.items():
            # print(label, sent)
            if sent not in sent2perplexity:
                perplexity = compute_perplexity(ref, tokenizer, model)
                sent2perplexity[sent] = perplexity
                perplexities[label] = perplexity
            else:
                perplexities[label] = sent2perplexity[sent]
        # print(perplexities)
        if perplexities["hyp1"] < perplexities["hyp2"]:
            hyp1_better += 1
        elif perplexities["hyp1"] > perplexities["hyp2"]:
            hyp2_better += 1
        else:
            equal += 1
    
    # save in pickle perplexities
    with open("pickle/perplexities.pkl", "wb") as file:
        pickle.dump(sent2perplexity, file)

    # print results
    print(filename1, "is better:", hyp1_better)
    print(filename2, "is better:", hyp2_better)
    print("equal:", equal)