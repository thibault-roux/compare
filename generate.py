# generate an html file to visualise difference between two ASR systems


"""
filename1 = "data/KD_woR.txt"
filename2 = "data/KD_wR.txt"
"""
filename1 = "ex1.txt"
filename2 = "ex2.txt"


def read(filename):
    ids = []
    refs = []
    hyps = []
    with open("data/" + filename, "r", encoding="utf8") as file:
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


txt = """<table>
    <tr>
        <td width="30"></td>
        <td width="300"></td>
        <td width="300"></td>
        <td width="300"></td>
      </tr>
    <tr>
		<td> <b>ID</b> </td>
		<td> <b>Reference</b> </td>
		<td> <b>Hypothesis 1</b> </td>
		<td> <b>Hypothesis 2</b> </td>
	</tr>
"""
for i in range(len(refs1)):
    txt += "\t<tr>\n"
    txt += "\t\t<td> " + ids1[i] + " </td>\n"
    txt += "\t\t<td> " + refs1[i] + " </td>\n"
    txt += "\t\t<td> " + hyps1[i] + " </td>\n"
    txt += "\t\t<td> " + hyps2[i] + " </td>\n"
    txt += "\t</tr>\n"
txt += "</table>\n"

with open("html/" + filename1[:-4] + "-" + filename2[:-4] + ".html", "w", encoding="utf8") as file:
    file.write(txt)

print("End of program.")