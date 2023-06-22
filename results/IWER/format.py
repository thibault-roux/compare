

files = ["fr", "ment", "tant", "tion"]
systems = ["SB_bpe1000","SB_bpe750", "SB_bpe500", "SB_bpe250", "SB_w2v_7k"]

results = dict()
for file in files:
    results[file] = dict()
    with open("iwer_words_" + file + ".txt", "r") as f:
        for line in f:
            system, iwer = line.strip().split(",")
            results[file][system] = float(iwer)

with open("total.csv", "w") as f:
    txt = "systems,"
    for file in files:
        txt += file + ","
    txt = txt[:-1] + "\n"
    for system in systems:
        txt += system + ","
        for file in files:
            txt += str(results[file][system]) + ","
        txt = txt[:-1] + "\n"
    f.write(txt)


# systems, iwer_fr, iwer_ment, iwer_tant, iwer_tion
# SB_bpe1000, 0.0, 0.0, 0.0, 0.0
# SB_bpe750, 0.0, 0.0, 0.0, 0.0
# SB_bpe500, 0.0, 0.0, 0.0, 0.0
# SB_bpe250, 0.0, 0.0, 0.0, 0.0