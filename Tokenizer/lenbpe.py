import matplotlib.pyplot as plt

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

if __name__ == '__main__':
    read_vocab('1000_bpe.vocab')
    read_vocab('750_bpe.vocab')
    read_vocab('500.vocab')
    read_vocab('250_bpe.vocab')