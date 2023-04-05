import numpy as np
from utils.leven import levenstein_alignment




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
    with open("../../metrics/hypereval/data/" + filename + "/" + filename + "1.txt", "r", encoding="utf8") as file:
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


def generate_html(filename1, filename2):
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

    txt = """<table border="1">\n\t<tr>\n\t\t<th>ID</th>\n\t\t<th>Reference</th>\n\t\t<th>Hypothesis 1</th>\n\t\t<th>Hypothesis 2</th>\n\t</tr>\n"""
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



if __name__ == "__main__":
    filename1 = "KD_woR"
    filename2 = "KD_wR"
    """
    filename1 = "ex1"
    filename2 = "ex2"
    """

    generate_html(filename1, filename2)