import sentencepiece as spm
from utils.leven import levenstein_alignment

def load_data(filename):
    refs = []
    hyps = []
    with open("data/" + filename, "r", encoding="utf8") as f:
        for line in f:
            line = line.split("\t")
            refs.append(line[1])
            hyps.append(line[2])
    return refs, hyps

def token_error_rate_local(ref, hyp, sp): # adapt this part using the sentence piece tokenizer
    ref_aligned, hyp_aligned, binary_list = levenstein_alignment(ref, hyp)
    errors = 0
    for i, word in enumerate(ref_aligned):
        if binary_list[i] == 0:
            errors += 1
    return errors, len(ref)

def token_error_rate(refs, hyps, sp):
    errors = 0
    length = 0
    for i, ref in enumerate(refs):
        ref = sp.encode(ref, out_type=str, enable_sampling=False)
        hyp = sp.encode(hyp, out_type=str, enable_sampling=False)
        e, l = token_error_rate_local(ref, hyp, sp)
        errors += e
        length += l
    return errors/length



if __name__ == "__main__":
    sp = spm.SentencePieceProcessor(model_file='Tokenizer/1000_bpe.model')

    systems = ["KD_woR","KD_wR","SB_bpe1000","SB_bpe750","SB_s2s","SB_w2v", "SB_w2v_1k","SB_w2v_3k","SB_w2v_7k","SB_xlsr_fr","SB_xlsr"]
    systems = ["SB_w2v_7k"]
    txt = ""
    for system in systems:
        print(system)
        txt += system + ","
        refs, hyps = load_data(system + "1.txt")
        ter = token_error_rate(refs, hyps, sp)
        print(ter)