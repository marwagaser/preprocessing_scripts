import re
import preprocessor as p
import emoji
p.set_options(p.OPT.URL, p.OPT.SMILEY)#1.emoji option removed as it messes up Arabic letters 2.do not include p.OPT.RESERVED,p.OPT.MENTION,p.OPT.HASHTAG
preprocessedtext = []
def keep_En_Ar(line): #remove any character that is neither English nor Arabic
    return re.sub(r'[^\x00-\x7F،-٩0-9]+',' ',line)
def removeHashtagsandMentionSymbol(line): #removes hashtags and mentions without removing word attached to it
    return re.sub(r"\#|\@","",line)
def unifyapostrophe(line):
    return re.sub('\’','\'',line)
def remove_emojis(text):
    return emoji.get_emoji_regexp().sub(r'', text)
def twitterprocessor(line):
    line = remove_emojis(line)
    return p.clean(line) #remove URL, hashtag, emoticons, and emojis
def tokenizeContractions(line):
    return re.sub(r"(n't|'(?:ll|[vr]e|[msd]))\b", r" \g<0>", line)#tokenize contractions
def tokenizeNumerics(line):
    return re.sub(r'(?<=[^0-9\s])(?=[0-9])|(?<=[0-9])(?=[^0-9\s])'," ",line)#tokenize numerics
def removeDuplicates(line):#remove more than two duplicates
    return re.sub(r"(.)\1+", r"\1\1", line) #remove >2 reptitions
def tokenizePunc(line):
    return re.sub(r"([^\w\s\'])", r' \1 ', line) #tokenize punctuation except apostrophe
# def chooseIntended(line):
#    return re.sub(r"\[\s*([^][|]*?)\s*\|[^][]*]", r"\1", line)
def removeextraspace(line):
    return re.sub('\s{2,}', ' ', line)
def lowercase(line):
    return line.lower()
def remove_trailing_leading_spaces(line):
    return line.strip()
def removeTypoCorrectionSign(line): #remove = sign before word
    return re.sub(r"([=])([a-zA-Z]+)",r"\2",line)
def removeBestTranslationSign(line):
    return re.sub(r"\(\s*\(\s*(.*?)\s*\)\s*\)",r"\1",line) #Remove (()) for best translation guess
def remove_tags(line):
    return re.sub(r"\<|\>|\«|\»","",line)
with open ("/home/marwagaser/c1.txt","r") as textfile:#(change file name here)
    for line in textfile:
        line = lowercase(remove_trailing_leading_spaces(removeextraspace(keep_En_Ar(removeHashtagsandMentionSymbol(remove_tags(removeBestTranslationSign(tokenizePunc(tokenizeContractions(tokenizeNumerics(removeDuplicates(removeTypoCorrectionSign(twitterprocessor(unifyapostrophe(line))))))))))))))
        preprocessedtext.append(line)
with open ("/home/marwagaser/c2.txt","w") as output: #change file name to store results in here
       corpora = "\n".join(preprocessedtext)
       output.write(corpora)
