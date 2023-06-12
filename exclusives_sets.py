from utils.io import read

# useful to generate sets of vocabulary specific to each corpus



if __name__ == "__main__":
    filename1 = "SB_bpe1000"
    filename2 = "SB_w2v_7k"
    data1 = read(filename1)
    data2 = read(filename2)

    vocab1 = set()
    vocab2 = set()

    for id, refhyp in data1.items():
        vocab2.update(data2[id][0].split())
        vocab2.update(data2[id][1].split())

    print(len(vocab1))
    print(len(vocab2))

    print(vocab1 - vocab2)
    print(vocab2 - vocab1)