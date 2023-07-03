import matplotlib.pyplot as plt
import numpy as np

# write a function that read a bpe vocab file and return a dictionary a list of length of tokens

def read_vocab(vocab_file):
    len_tokens = []
    with open(vocab_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            token, index = line.split('\t')
            len_tokens.append(len(token))
    # plot_len_tokens(len_tokens, vocab_file.split('_')[0])
    with open('hist/' + vocab_file.split(".vocab")[0] + ".csv", 'w') as f:
        for length in len_tokens:
            f.write(str(length) + '\n')
    return len_tokens

# write a function that receives a list of length of tokens and save a plot of the distribution of the length of tokens

def plot_len_tokens(len_tokens, num):
    plt.hist(len_tokens, bins=100)
    # plt.xlim(0, 100)
    plt.ylim(0, 250)
    plt.xlabel('Length of tokens')
    plt.ylabel('Frequency')
    plt.title('Distribution of the length of tokens for BPE vocab of size {}'.format(num))
    plt.savefig("hist/" + num + '.png')
    plt.clf()

def plot_all_len_tokens(len_tokens_all):
    colors = ["#4285f4", "#ea4335", "#fbbc05", "#34a853"]
    plt.hist(len_tokens_all, bins=np.linspace(0.5, 9.5, 10), label=['BPE 1000', 'BPE 750', 'BPE 500', 'BPE 250'], color=colors)
    plt.xticks(np.linspace(1, 10, 10))
    plt.legend()
    # plt.xlim(0, 100)
    plt.ylim(0, 250)
    plt.xlabel('Length of tokens')
    plt.ylabel('Frequency')
    plt.title('Distribution of the length of tokens for BPE')
    plt.savefig("hist/all.svg")
    plt.clf()



if __name__ == '__main__':
    len_toks_all = []
    len_toks_all.append(read_vocab('1000_bpe.vocab'))
    len_toks_all.append(read_vocab('750_bpe.vocab'))
    len_toks_all.append(read_vocab('500_bpe.vocab'))
    len_toks_all.append(read_vocab('250_bpe.vocab'))

    plot_all_len_tokens(len_toks_all)