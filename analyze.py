from collections import OrderedDict
from utils.io import read, intersect

# this code has the purpose to study the most common words in the reference

def common_words(data, filename):
    words1 = dict()
    for id, refhyp in data1.items():
        for word in refhyp[0].split(" "):
            if word in words1:
                words1[word] += 1
            else:
                words1[word] = 1

    # sort words by frequency
    words2 = OrderedDict(sorted(words1.items(), key=lambda x: x[1], reverse=True))
    with open("results/" + filename + "_common_words.txt", "w", encoding="utf8") as file:
        for word, freq in words2.items():
            file.write(word + "\t" + str(freq) + "\n")

    chain = "t"
    with open("data/words_" + chain + ".txt", "w", encoding="utf8") as file:
        for word, freq in words2.items():
            if freq >= 10 and chain in word:
                for index in range(len(word)):
                    if word[index] == chain:
                        file.write(word + "\t" + str(freq) + "\n")
                        print(word, freq)
                        break

                    # if index > 0:
                    #     if word[index-1] not in "aeiouyéèà" and word[index] == chain:
                    #         if index+1 == len(word):
                    #             file.write(word + "\t" + str(freq) + "\n")
                    #             print(word, freq)
                    #             break
                    #         elif word[index+1] not in "aeiouyéèà":
                    #             file.write(word + "\t" + str(freq) + "\n")
                    #             print(word, freq)
                    #             break


if __name__ == "__main__":
    filename1 = "SB_bpe1000"
    filename2 = "SB_w2v_7k"
    filename3 = "SB_bpe750"
    data1 = read(filename1)
    data2 = read(filename2)
    data3 = read(filename3)
    data1, data2 = intersect(data1, data2)
    data1, data3 = intersect(data1, data3)
    data2, data3 = intersect(data2, data3)

    common_words(data1, filename1)
    # common_words(data2, filename2)
    # common_words(data3, filename3)