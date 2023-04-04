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
    return errors, len(ref.split(" "))

def WER(ref, hyp):
    ref_aligned, hyp_aligned, binary_list = levenstein_alignment(ref.split(" "), hyp.split(" "))
    errors = 0
    for i, word in enumerate(ref_aligned):
        if binary_list[i] == 0:
            errors += 1
    return errors, len(ref.split(" "))


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
        if c not in " éèêçâàîïôùûabcdefghijklmnopqrstuvwxyz0123456789'":
            string = string.replace(c, "")
    return string

def load_data(filename):
    refs = []
    hyps = []
    with open("data/" + filename, "r", encoding="utf8") as f:
        for line in f:
            line = line.split("\t")
            refs.append(line[1])
            hyps.append(line[2])
    return refs, hyps

def wer(refs, hyps, clean=True):
    errors_total = 0
    length_total = 0
    for ref, hyp in zip(refs, hyps):
        if clean:
            errors, length = WER(clean_string(ref), clean_string(hyp))
        else:
            errors, length = WER(ref, hyp)
        errors_total += errors
        length_total += length
    return errors_total / length_total * 100


def some_wer(refs, hyps):
    worse = 0
    better = 0
    equal = 0
    for ref, hyp in zip(refs, hyps):
        errors_clean, length_clean = WER(clean_string(ref), clean_string(hyp))
        errors_unclean, length_unclean = WER(ref, hyp)
        clean = errors_clean/length_clean
        unclean = errors_unclean/length_unclean
        if clean > unclean: # clean is worse
            worse += 1
        elif clean < unclean: # clean is better
            better += 1
        else: # clean is equal
            equal += 1
    print("clean worse: ", worse)
    print("clean better: ", better)
    print("clean equal: ", equal)
    

def iwer(refs, hyps, words):
    errors_total = 0
    length_total = 0
    for ref, hyp in zip(refs, hyps):
        errors, length = IWER(ref, hyp, words)
        errors_total += errors
        length_total += length
    return errors_total / length_total * 100


if __name__ == "__main__":
    # print(IWER("ceci est un exemple", "ce ceci est une exemple pas", {"<epsilon>", "ce", "ceci", "est", "un", "une", "exemple", "pas"}))

    refs, hyps = load_data("KD_woR.txt")
    some_wer(refs, hyps)
    exit()
    print(wer(refs, hyps))
    print(wer(refs, hyps, clean=False))