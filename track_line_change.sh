#!/bin/bash
#date 17.10.2021
#author Marwa Gaser
#The script has three commands. First: it finds the difference between two files#Then it deletes every other line bc the diff command generates unwanted lines
#Then we keep the last number of each line

read file1
read file2
read file3
diff "$file1" "$file2" > "$file3"
sed -e n\;d < $"file3" > TBD.txt
grep -Eo '[0-9]+$' <TBD.txt > "$file3"
#END
