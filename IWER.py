from utils.leven import levenstein_alignment

# Using the levenstein_alignment function, calculate the IWER
# It computes the number of errors on specific words contained in a list
# the IWER is this number divided by the number of words in the reference

def IWER(ref, hyp, words):
    ref_aligned, hyp_aligned, binary_list = levenstein_alignment(ref.split(" "), hyp.split(" "))
    errors = 0
    for i, word in enumerate(ref_aligned):
        if word in words and binary_list[i] == 0:
            errors += 1
    return errors / len(ref.split(" ")) * 100

def WER(ref, hyp, words):
    ref_aligned, hyp_aligned, binary_list = levenstein_alignment(ref.split(" "), hyp.split(" "))
    errors = 0
    for i, word in enumerate(ref_aligned):
        if binary_list[i] == 0:
            errors += 1
    return errors / len(ref.split(" ")) * 100


# function that cleans a string reference from uncommon accents and encoding bugs
def clean_string(string):
    string = string.lower()
    string = string.replace("’", "'")
    string = string.replace("œ", "oe")
    string = string.replace("æ", "ae")
    string = string.replace("«", "")
    string = string.replace("»", "")
    string = string.replace("(", "")
    string = string.replace(")", "")
    string = string.replace("-", " ")
    for c in set(string):
        if c not in "éèêçâàîïôùûabcdefghijklmnopqrstuvwxyz0123456789'":
            string = string.replace(c, "")
    return string

def load_data(filename, clean=True):
    ref = []
    hyp = []
    with open("data/" + filename, "r", encoding="utf8") as f:
        for line in f:
            line = line.split("\t")
            if clean:
                ref.append(clean_string(line[1]))
                hyp.append(clean_string(line[2]))
            else:
                ref.append(line[1])
                hyp.append(line[2])



if __name__ == "__main__":
    # print(IWER("ceci est un exemple", "ce ceci est une exemple pas", {"<epsilon>", "ce", "ceci", "est", "un", "une", "exemple", "pas"}))

