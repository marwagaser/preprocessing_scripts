import re

def removeDoubleParentheses(line):
    return re.sub(r"\(\s*\(\s*(.*?)\s*\)\s*\)",r"\1",line) #Remove (()) for best translation guess
def removeAnnotations(line): #
    return re.sub(r"(\/\/)|\=|\#|\+|\*|\@|\$"," ",line)
def removeTags(line): 
    return re.sub(r"(?i)(\(|\[)\s*(LAUGHTER|COUGH|NOISE|HES|HUM|BREATH)\s*(\)|\}|\])","",line)
def remove_partial_words(line):
    return re.sub(r"\%\w+","",line)
preprocessedtext=[]
with open ("/home/marwagaser/OCT_corpora/corpora/checked/ArzEn/raw/camel_clean/test_clean.tgt","r") as textfile:#(change file name here)
    for line in textfile:
        line = line.strip()
        line = remove_partial_words(removeAnnotations(removeTags(removeDoubleParentheses(line))))
        preprocessedtext.append(line)
        
with open ("/home/marwagaser/OCT_corpora/corpora/checked/ArzEn/raw/camel_clean/annotation_free/test_clean_annotation_free.tgt","w") as output: #change file name to store results in here
       corpora = "\n".join(preprocessedtext)
       output.write(corpora)