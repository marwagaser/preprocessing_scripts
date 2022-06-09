import re
import sys
import os
blank_line_regex = r"(?:\r?\n){2,}"
def select_lines(text, keyword):
    chunks_needed = []
    paras = re.split(blank_line_regex,text.strip())
    for para in paras:
        if ( para.startswith(keyword)):
          chunks_needed.append( para )

    return chunks_needed

allwords=[]


allwords=[]
# text_file = open("file2.txt")
# text_file_string = text_file.read()
# target_paragraphs = select_lines(text_file_string,"CHUNK")
import os

for filename in os.listdir('integrated'):
        with open(os.path.join('integrated', filename)) as f:
            text_file_string = f.read()
            target_paragraphs = select_lines(text_file_string,"CHUNK")
            for target_paragraph in target_paragraphs: #for each paragraph
              s_list=[]
              t_list=[]
              for line in target_paragraph.split("\n"): #for each line in that paragraph
                is_source = re.compile(r'^s:\d+')
                is_target = re.compile(r'^t:\d+')
                if is_source.search(line):
                  s_list.append(line)
                elif is_target.search(line):
                  t_list.append(line)
              for s in s_list: # for each s reterived from that line
                sen_s_list = s.split("·")
                arabic_unsegmented_word = sen_s_list[1]
                start_index_of_seg = int(sen_s_list[5])
                end_index_of_seg = int(sen_s_list[6])
                #store arabic unsegmented in file and follow it by a tab
                temp_t=[]
                for index in range(start_index_of_seg,end_index_of_seg+1):
                  temp_t.append(t_list[index].split("·")[-3])
                segmented_arabic_word = (" ".join(map(str, temp_t)))
                finalword=arabic_unsegmented_word+"\t"+segmented_arabic_word
                allwords.append(finalword)
                

with open ("op.txt","w") as output: #file to store the results in
	output.write("\n".join(map(str, allwords)))
  

