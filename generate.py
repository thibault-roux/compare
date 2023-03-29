import numpy as np

# generate an html file to visualise difference between two ASR systems

def levenstein_alignment(ref, hyp):
    # create a matrix of size (len(ref)+1) x (len(hyp)+1)
    # the first row and the first column are filled with 0, 1, 2, 3, ...
    # the rest of the matrix is filled with -1
    matrix = np.zeros((len(ref)+1, len(hyp)+1))
    for i in range(1, len(ref)+1):
        matrix[i, 0] = i
    for j in range(1, len(hyp)+1):
        matrix[0, j] = j
    for i in range(1, len(ref)+1):
        for j in range(1, len(hyp)+1):
            matrix[i, j] = -1

    # fill the matrix with the correct values
    for i in range(1, len(ref)+1):
        for j in range(1, len(hyp)+1):
            if ref[i-1] == hyp[j-1]:
                matrix[i, j] = matrix[i-1, j-1]
            else:
                matrix[i, j] = min(matrix[i-1, j-1], matrix[i-1, j], matrix[i, j-1]) + 1

    # create two lists of words with a <epsilon> token for insertion and deletion
    ref_aligned = []
    hyp_aligned = []
    i = len(ref)
    j = len(hyp)
    while i > 0 or j > 0:
        if i > 0 and j > 0 and ref[i-1] == hyp[j-1]:
            ref_aligned.append(ref[i-1])
            hyp_aligned.append(hyp[j-1])
            i -= 1
            j -= 1
        elif i > 0 and matrix[i, j] == matrix[i-1, j] + 1:
            ref_aligned.append(ref[i-1])
            hyp_aligned.append("<epsilon>")
            i -= 1
        elif j > 0 and matrix[i, j] == matrix[i, j-1] + 1:
            ref_aligned.append("<epsilon>")
            hyp_aligned.append(hyp[j-1])
            j -= 1
        else:
            ref_aligned.append(ref[i-1])
            hyp_aligned.append(hyp[j-1])
            i -= 1
            j -= 1

    refa, hypa = ref_aligned[::-1], hyp_aligned[::-1]
    binary_list = [int(r == h) for r, h in zip(refa, hypa)]
    return refa, hypa, binary_list



# write a function taking a list of words and a list of 0 and 1 and returning a string with the words in red if the corresponding value is 0 and in green if the corresponding value is 1 for html

def color_html(ref, hyp):
    ref, hyp, binary_list = levenstein_alignment(ref.split(), hyp.split())
    txt = ""
    for h, b in zip(hyp, binary_list):
        if b == 1:
            # txt += "<span style='color: green'>" + h + "</span> "
            txt += h + " "
        else:
            txt += "<span style='color: red'>" + h + "</span> "
    return txt[:-1]

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


def intersect(data1, data2):
    new_data1 = dict()
    new_data2 = dict()

    for id, refhyp in data1.items():
        if id in data2:
            ref = refhyp[0]
            if ref == data2[id][0]: # check if both refs are the same
                new_data1[id] = [ref, data1[id][1]]
                new_data2[id] = [ref, data2[id][1]]
    return new_data1, new_data2


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
    data1, data2 = intersect(data1, data2)

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



    txt = """<table border="1">
    <tr>
        <th>ID</th>
        <th>Reference</th>
        <th>Hypothesis 1</th>
        <th>Hypothesis 2</th>
    </tr>
"""
    for id, refhyp in data1.items():
        ref = refhyp[0]
        hyp1 = refhyp[1]
        hyp2 = data2[id][1]
        txt += "\t<tr>\n"
        txt += "\t\t<td> " + id + " </td>\n"
        txt += "\t\t<td> " + ref + " </td>\n"
        txt += "\t\t<td> " + color_html(ref, hyp1) + " </td>\n"
        txt += "\t\t<td> " + color_html(ref, hyp2) + " </td>\n"
        txt += "\t</tr>\n"
    txt += "</table>\n"

    with open("html/" + filename1[:-4] + "-" + filename2[:-4] + ".html", "w", encoding="utf8") as file:
        file.write(txt)

    print("End of program.")



