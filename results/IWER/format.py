

files = ["fr", "ment", "tant", "tion"]
systems = ["SB_bpe1000","SB_bpe750", "SB_bpe500", "SB_bpe250", "SB_w2v_7k"]

results = dict()
for file in files:
    results[file] = dict()
    with open("iwer_words_" + file + ".txt", "r") as f:
        for line in f:
            system, iwer = line.strip().split(",")
            results[file][system] = float(iwer)

with open("total.txt", "w") as f:
    file.write(",")
    for file in files:
        f.write(file + "\n")
        for system in systems:
            f.write(system + ": " + str(results[file][system]) + "\n")
        f.write("\n")
