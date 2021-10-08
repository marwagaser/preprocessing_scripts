from sacremoses import MosesDetokenizer
md = MosesDetokenizer(lang='en')
import re
def detokenizeCombinedWords(line):
    line = re.sub(r'\b(can)(\s)(not)\b', 'cannot',line)
    line = re.sub(r'\b(gon)(\s)(na)\b', 'gonna',line)
    return re.sub(r'\b(wan)(\s)(na)\b', 'wanna',line)
def detokenizeContractions(line):
    #convert all ’ into ' then detokenize contractions
    line = re.sub('\’','\'',line)
    return re.sub(r"\s(n't|'(?:ll|[vr]e|[msd]))\b", r"\1", line)#detokenize contractions
def detokenizeDashes(line):
    return re.sub(r"(\s)(-)(\s)",r"\2",line)#removes space around hyphen
detok = []
with open ("/home/marwagaser/c2.txt","r") as textfile:#(change file name here)
    for line in textfile:
        line_list = line.split(" ")
        new_line = md.detokenize(line_list) #detokenize using Moses Detokenizer
        new_line = detokenizeContractions(new_line) #detokenize contractions like do n't because Moses Detokenizer doesn't do that
        new_line = detokenizeDashes(new_line) #remove the space before a (-) because Moses Detokenizer doesn't do that
        detok.append(new_line)

with open ("/home/marwagaser/c3.txt","w") as output: #change file name to store results in here
       corpora = "\n".join(detok)
       output.write(corpora)