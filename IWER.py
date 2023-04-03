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
    return errors / len(ref)

# print(levenstein_alignment("ceci est un exemple".split(" "), "ce ceci est une exemple pas".split(" ")))