#arabic_unicode = '[\u0621-\u064A\u0660-\u0669 ]+'

import re
def keep_En_Ar(line):
    return re.sub(r'[^\x00-\x7F،-٩0-9]+',' ',line)
def remove_non_English_chars(line):
    return re.sub(r'[^\x00-\x7F]+',' ', line)
def remove_non_Arabic_chars(line):
    return re.sub(r'[،-٩0-9]+',' ', line)
print(keep_En_Ar('here is a trial 123 ☺  ♈ @@@ محاولة ü !!!!!!!!! '))