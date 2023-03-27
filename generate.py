# generate an html file to visualise difference between two ASR systems




def read(filename):
    data = dict()
    with open("data/" + filename, "r", encoding="utf8") as file:
        for line in file:
            line = line.split("\t")
            id = line[0]
            ref = line[1]
            hyp = line[2]
            data[id] = [ref, hyp]
    return data


def intersect(ids1, refs1, hyps1, ids2, refs2, hyps2):
    new_ids = []
    new_refs = []
    new_hyps1 = []
    new_hyps2 = []

    for i in range(len(ids1)):
        if ids1[i] in ids2:
            if refs1[i] in refs2:
                new_ids.append(ids1[i])
                new_refs.append(refs1[i])
                new_hyps1.append()


if __name__ == "__main__":
    filename1 = "KD_woR.txt"
    filename2 = "KD_wR.txt"
    """
    filename1 = "ex1.txt"
    filename2 = "ex2.txt"
    """

    print("Loading dataset...")
    data1 = read(filename1)
    data2 = read(filename2)

    for k1, v1 in data1.items():
        if k1 not in data2:
            raise Exception("ids are not the same. Check first column of data.")
        if v1[0] != data2[k1][0]:
            raise Exception("refs are not the same. Check second column of data.")
    for k2, v2 in data2.items():
        if k2 not in data1:
            raise Exception("ids are not the same. Check first column of data.")
        if v2[0] != data1[k2][0]:
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
    for id, refhyp in data1.items():
        ref = refhyp[0]
        hyp1 = refhyp[1]
        hyp2 = data2[id][1]
        txt += "\t<tr>\n"
        txt += "\t\t<td> " + id + " </td>\n"
        txt += "\t\t<td> " + ref + " </td>\n"
        txt += "\t\t<td> " + hyp1 + " </td>\n"
        txt += "\t\t<td> " + hyp2 + " </td>\n"
        txt += "\t</tr>\n"
    txt += "</table>\n"

    with open("html/" + filename1[:-4] + "-" + filename2[:-4] + ".html", "w", encoding="utf8") as file:
        file.write(txt)

    print("End of program.")