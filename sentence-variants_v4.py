'''
Usage: python3 sentence-variants.py [in_file] [out_file]
python3 sentence-variants.py trg src
'''

import re
import itertools
import sys
en_corpus = []
ar_corpus = []
lineNumber = []
def permute_intendedonly_transliteratedonly(listA): #keeps all intended or all transliterated
       permutations_list = []
       permutations_list.append([item[0] for item in listA])
       permutations_list.append([item[1] for item in listA])
       return permutations_list
def permute(*args):
       permutations_list = []
       for single_list in itertools.product(*lists): 
           perm_sublist=[]
           for value in single_list:
               perm_sublist.append(value)
           permutations_list.append(perm_sublist)
       return permutations_list
def regexFound(line):
    regexp = re.compile(r"\[\s*([^][|]*?)\s*\|([^][]*?)\s*]")
    if regexp.search(line):
        return True
    return False
def countOccurrence(line):
   return len(re.findall(r"\[\s*([^][|]*?)\s*\|[^][]*]", line))
def numberOfChoice(line):
    num = countOccurrence(line)
    list_template = [r"\1",r"\2"]
    return [list_template for x in range(0,num)]

#now create n sentences for n permutations
                                                    
def generateSentences(listA, line):
    permuted_sentences = []
    numberOfSentences = len(listA)
    for a_permute in listA:
       #print(a_permute)
       templine = line
       for x in range (0,len(a_permute)):
           templine = re.sub(r"\[\s*([^][|]*?)\s*\|\s*([^][]*?)\s*]", a_permute[x], templine, 1)
       permuted_sentences.append(templine)
    return permuted_sentences
#keep track of the line number and then when you rra

ar_file_lines=open(sys.argv[2]).readlines() #arabic file
with open (sys.argv[1]) as textfile: #english file
     counter = 0
     dict_multiple_translation_count={}
     dict_multiple_translation_count[0]=0
     for line in textfile:
         if len(line.strip()) != 0  and len(ar_file_lines[counter].strip()) != 0 :
                en_line = line.strip()
                en_line_info = line.split("\t")
                en_line_id = en_line_info[0]
                en_line_text = en_line_info[1]
                ar_line = ar_file_lines[counter].strip()
                ar_line_info = ar_file_lines[counter].split("\t")
                ar_line_id = ar_line_info[0]
                ar_line_text = ar_line_info[1]

                # checking ar and en sentences both have same IDs
                if en_line_id != ar_line_id:
                    print("################# ERROR in line: "+en_line_id+" #################")
                    continue # ignore this sentence
                counter+=1 
                if (regexFound(en_line_text)):
                    lists = numberOfChoice(en_line_text) #this is going to be created by knowing how many occurrences we have 
                    if len(lists) in dict_multiple_translation_count:
                        dict_multiple_translation_count[len(lists)]=dict_multiple_translation_count[len(lists)]+1
                    else:
                        dict_multiple_translation_count[len(lists)]=1
                    if len(lists)>4:
                        print(en_line_id+"\t"+str(len(lists)))
                    else:
                        x = permute_intendedonly_transliteratedonly(lists) #get all possible permutations
                        generated_sentences_list = generateSentences(x,en_line_text)
                        generated_sentences_index = 0
                        for sent in generated_sentences_list:
                            en_corpus.append(en_line_id+"_"+str(generated_sentences_index)+"\t"+sent.strip())
                            ar_corpus.append(en_line_id+"_"+str(generated_sentences_index)+"\t"+ar_line_text.strip())
                            generated_sentences_index+=1
                        lineNumber.append([counter,len(generated_sentences_list)])
                else:
                    dict_multiple_translation_count[0]=dict_multiple_translation_count[0]+1
                    en_corpus.append(en_line)
                    ar_corpus.append(ar_line)
for k, v in sorted(dict_multiple_translation_count.items()):
    print(str(k)+":"+str(v))
                 
with open (sys.argv[1]+"_muliple_translations","w") as output:#save English version
         output.write("\n".join(map(str, en_corpus)))

with open (sys.argv[2]+"_muliple_translations","w") as output:#save Arabic version
         output.write("\n".join(map(str, ar_corpus)))

