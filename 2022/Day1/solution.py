
from audioop import reverse
import re

def split_on_empty_lines(s):

    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"

    return re.split(blank_line_regex, s.strip())

f= open('input.txt', 'r').read()
cate=split_on_empty_lines(f)

#print(cate)

total = []

for n in cate:
    #print(cate[0].split("\n"))
    b=n.split("\n")
    tot =0
    for bi in b:
        tot = tot + int(bi)
    total.append(tot)
#print(total)
#part1
print(max(total))
#part2
total.sort(reverse=True)
sum = total[0]+total[1]+total[2]
print(sum)
