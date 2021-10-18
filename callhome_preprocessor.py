import re
def removeTalkNoise(line): # (considers any bracket combination too) removes noise in CALLHOME like {laugh}, {sneeze}, {breath}, {lipsmack}, [distortion], [static], [background]
    return re.sub(r"(?i)(\(|\{|\[)\s*(laugh|sneeze|cough|breath|lipsmack)\s*(\)|\}|\])","",line)
def removeIntermittentNoise(line): #removes noise in CALLHOME like [/static] [static/]
    return re.sub(r"(?i)(\[|\<|\{|\()(\/)?\s*(distortion|static|background|aside|overlap)\s*(\]|\>|\)|\})|(\[|\<|\{|\()\s*(distortion|static|background|aside|overlap)\s*(\/)?(\]|\>|\)|\})","",line)
def removeDoubleParentheses(line):
    return re.sub(r"\(\s*\(\s*[^(]*\s*\)\s*\)","",line) #Remove (()) and its content
def removeDoubleSquareParentheses(line):
    return re.sub(r"(?i)\[\s*\[\s*(background|drawn out)\s*\]\s*\]","",line) #Remove [[]] and its content
def removeDoubleAsterisk(line):
    return re.sub(r"\*{2}(.*?)\*{2}","",line) #Remove **text**
def removeLanguageTags_European_and_English(line):
    return re.sub(r"(?i)(\<|\()\s*(English|French|Italian)(\s*)(.*?)\s*(\)|\>)",r" \4 ",line) #Remove <English text> -> text
def removeLanguageTags_MSA_and_Others(line):
    return re.sub(r"(?i)(\<|\()\s*(MSA|Delta|Upper)(\s*)(.*?)\s*(\)|\>)","",line) #Remove <MSA text> -> ""
def removePartialwords(line):
    return re.sub(r'(?<!\S)(-\S+-)(?!\S)|(?<!\S)-\S+(?![\S-])|(?<![\S-])\S+-(?!\S)', r'\1', line)
def removeProperNounAnnotation(line):
    return re.sub(r'(?<!\S)&(\S+)(?![\S&])', r"\1", line)
def removeTrailingandLeadingDoubleHyphens(line):
    # remove -- in -> -- translated sentence -- -> translated sentence
    return re.sub(r"(\t\-\-)|(\-\-$)","\t",line)
preprocessedtext=[]

with open ("/home/marwagaser/preprocessing_scripts/tgt_4","r") as textfile:#(change file name here)
    for line in textfile:
        line = line.strip()
        line = removePartialwords(removeProperNounAnnotation(removeLanguageTags_MSA_and_Others(
            removeLanguageTags_European_and_English(
            removeDoubleAsterisk(
                removeIntermittentNoise(
                    removeTalkNoise(
                removeDoubleSquareParentheses(
                    removeDoubleParentheses(removeTrailingandLeadingDoubleHyphens(line))
                    )
                    )
                    )
                    )
                    )
                    )))
        
        
        preprocessedtext.append(line)
with open ("/home/marwagaser/preprocessing_scripts/tgt_4_2","w") as output: #change file name to store results in here
       corpora = "\n".join(preprocessedtext)
       output.write(corpora)