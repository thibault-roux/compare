# generate an html file to visualise difference between two ASR systems


"""
filename1 = "data/KD_woR.txt"
filename2 = "data/KD_wR.txt"
"""
filename1 = "data/ex1.txt"
filename2 = "data/ex2.txt"


def read(filename):
    ids = []
    refs = []
    hyps = []
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            line = line.split("\t")
            ids.append(line[0])
            refs.append(line[1])
            hyps.append(line[2])
    return ids, refs, hyps

print("Loading dataset...")
ids1, refs1, hyps1 = read(filename1)
ids2, refs2, hyps2 = read(filename2)

if ids1 != ids2:
    raise Exception("ids are not the same. Check first column of data.")

if refs1 != refs2:
    raise Exception("refs are not the same. Check second column of data.")