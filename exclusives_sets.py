from utils.io import read, intersect

# useful to generate sets of vocabulary specific to each corpus



if __name__ == "__main__":
    filename1 = "SB_bpe1000"
    filename2 = "SB_w2v_7k"
    data1 = read(filename1)
    data2 = read(filename2)
    data1, data2 = intersect(data1, data2)

    dico_list = dict()
    dico_list[filename1] = []
    dico_list[filename2] = []

    vocab1 = set()
    vocab2 = set()
    for id, refhyp in data1.items():
        vocab1.update(data1[id][1].split())
        dico_list[filename1] += data1[id][1].split()
        vocab2.update(data2[id][1].split())
        dico_list[filename2] += data2[id][1].split()


    exclusive_vocab = dict()
    exclusive_vocab[filename1] = sorted(vocab1 - vocab2)
    exclusive_vocab[filename2] = sorted(vocab2 - vocab1)

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