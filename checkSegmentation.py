import re
import sys
from camel_tools.utils.normalize import normalize_alef_ar
from camel_tools.utils.normalize import normalize_alef_maksura_ar
word_pairs = []

with open (sys.argv[1],"r") as textfile:
    for line in textfile:
        line = normalize_alef_maksura_ar(normalize_alef_ar(line.strip()))
        words_list = line.split('\t')
        word1 = words_list[0]
        word1_normalized = re.sub(r'\-|\s',"",word1)
        word2 = words_list[1]
        word2_normalized = re.sub(r'\-|\s',"",word2)
        if (word1_normalized==word2_normalized):
            line = word1 +"\t"+word2
            word_pairs.append(line)
with open (sys.argv[2],"w") as output:
	output.write('\n'.join(word_pairs)+"\n")

