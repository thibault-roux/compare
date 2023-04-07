import matplotlib.pyplot as plt

# write a function that read a bpe vocab file and return a dictionary a list of length of tokens

def read_vocab(vocab_file):
    vocab = {}
    with open(vocab_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            token, index = line.split('\t')
            vocab[token] = index
    plot_len_tokens(len_tokens, vocab_file.split('_')[0])
    return vocab

# write a function that receives a list of length of tokens and save a plot of the distribution of the length of tokens

def plot_len_tokens(len_tokens, num):
    plt.hist(len_tokens, bins=100)
    plt.xlabel('Length of tokens')
    plt.ylabel('Frequency')
    plt.title('Distribution of the length of tokens for BPE vocab of size {}'.format(num))
    plt.savefig("hist/" + num + '.png')

if __name__ == '__main__':
    vocab = read_vocab('1000_bpe.vocab')
    vocab = read_vocab('750_bpe.vocab')