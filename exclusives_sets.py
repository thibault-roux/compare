from utils.io import read, intersect

# useful to generate sets of vocabulary specific to each corpus



def exclusive_sets():
    filename1 = "SB_bpe1000"
    filename2 = "SB_w2v_7k"
    data1 = read(filename1)
    data2 = read(filename2)
    data1, data2 = intersect(data1, data2)

    dico_list = dict()
    dico_list[filename1] = []
    dico_list[filename2] = []

    vocab_reference = set()

    vocab1 = set()
    vocab2 = set()
    for id, refhyp in data1.items():
        vocab_reference.update(data1[id][0].split())
        vocab1.update(data1[id][1].split())
        dico_list[filename1] += data1[id][1].split()
        vocab2.update(data2[id][1].split())
        dico_list[filename2] += data2[id][1].split()


    exclusive_vocab = dict()
    exclusive_vocab[filename1] = sorted(vocab1 - vocab2 - vocab_reference)
    exclusive_vocab[filename2] = sorted(vocab2 - vocab1 - vocab_reference)

    # print sorted list of vocab1 and vocab2

    # for i, word1 in enumerate(exclusive_vocab1):
    #     word2 = exclusive_vocab2[i]
    #     print(word1, word2)
    #     input()

    print(dico_list[filename1][0])

    for filename in [filename1, filename2]:
        with open("results/" + filename + "_exclusive_vocab.txt", "w", encoding="utf8") as file:
            for word in exclusive_vocab[filename]:
                file.write(word + "," + str(dico_list[filename].count(word)) + "\n")

    # ne pas faire ça, générer juste l'exclusion (sans prendre en compte l'intersection de deux systèmes)




def original_vocab(filename):
    data = read(filename)

    with open("/local_disk/atlantia/laboinfo/rouvier/lm/vocab/uniq.old", "r", encoding="utf8") as file:
        vocab_to_delete = set(file.read().split())

    vocab_reference = set()
    vocab_hypothesis = set()
    for id, refhyp in data.items():
        vocab_reference.update(data[id][0].split())
        vocab_hypothesis.update(data[id][1].split())
    
    exclusive_vocab = sorted(vocab_hypothesis - vocab_reference - vocab_to_delete)

    with open("results/" + filename + "_exclusive_reference.txt", "w", encoding="utf8") as file:
        for word in exclusive_vocab:
            file.write(word + "\n")


if __name__ == "__main__":
    # exclusive_sets()

    original_vocab("SB_bpe750")
    original_vocab("SB_bpe1000")
    original_vocab("SB_w2v_7k")