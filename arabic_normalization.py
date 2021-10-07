#contractions tokenization?
from camel_tools.utils.dediac import dediac_ar
from camel_tools.tokenizers.word import simple_word_tokenize


from camel_tools.utils.normalize import normalize_alef_maksura_ar
from camel_tools.utils.normalize import normalize_alef_ar
import re

tokenized = []
def ortho_normalize(text):
    text = normalize_alef_maksura_ar(text)
    text = normalize_alef_ar(text)
    return text
def remove_diacritics(text):
     return dediac_ar(text)
with open ("/home/marwagaser/corpora/Round3/Round3/LDC2021T15/LDC2021T15_1.eg") as textfile: #enter file name here
    for line in textfile:
      line = ortho_normalize(remove_diacritics(line))
      line = ' '.join(line)
      line = re.sub('\s{2,}', ' ', line) #remove extra spaces in the line
      tokenized.append(line)
with open ("/home/marwagaser/corpora/Round3/Round3/LDC2021T15/LDC2021T15_2.eg","w") as output: #file to store the results in
        output.write("\n".join(map(str, tokenized)))

        