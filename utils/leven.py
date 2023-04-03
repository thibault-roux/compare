
import numpy as np


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