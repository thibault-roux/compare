



def count_error_type(filename):
    sub = 0
    ins = 0
    dels = 0
    egal = 0
    with open("../../metrics/hypereval/data/" + filename + "/" + filename + "2.txt", "r", encoding="utf8") as file:
        for line in file:
            line = line.split("\t")
            error_type = line[2]
            for error in error_type.split(" "):
                if error == "S":
                    sub += 1
                elif error == "I":
                    ins += 1
                elif error == "D":
                    dels += 1
                elif error == "=":
                    egal += 1
    print(sub + dels + egal)
    return sub, ins, dels, egal


if __name__ == "__main__":
    filename1 = "SB_w2v_7k"
    filename2 = "SB_bpe1000"
    filename3 = "SB_bpe750"

    print(filename1, count_error_type(filename1))
    print(filename2, count_error_type(filename2))
    print(filename3, count_error_type(filename3))

