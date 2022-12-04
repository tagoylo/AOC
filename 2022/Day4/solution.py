import re
import string            

def split_on_empty_lines(s):

    blank_line = r"(?:\r?\n){2,}"
    two_blank_line = r"(?:\r?\n){3,}"
    new_line = r"\r\n|\r|\n"
    character = r"[a]"

    return re.split(new_line, s.strip())

f= open('input.txt', 'r').read()
elves=split_on_empty_lines(f)
#print(elves)

total = 0
for n in elves:
    sec1 = n.split(",")[0]
    sec2 = n.split(",")[1]
    sec11 = sec1.split("-")[0]
    sec12 = sec1.split("-")[1]
    sec21 = sec2.split("-")[0]
    sec22 = sec2.split("-")[1]
    one = list(range(int(sec11), int(sec12)+1))
    two = list(range(int(sec21), int(sec22)+1))
    #print(one)
    #print(two)
    if set(one).issubset(set(two)) or set(two).issubset(set(one)):
        total = total + 1
    else:
        total = total

print("part1 :" +str(total))

total2 = 0
for n in elves:
    sec1 = n.split(",")[0]
    sec2 = n.split(",")[1]
    sec11 = sec1.split("-")[0]
    sec12 = sec1.split("-")[1]
    sec21 = sec2.split("-")[0]
    sec22 = sec2.split("-")[1]
    one = list(range(int(sec11), int(sec12)+1))
    two = list(range(int(sec21), int(sec22)+1))
    #print(one)
    #print(two)
    if set(one).intersection(set(two)):
        total2 = total2 + 1
    else:
        total2 = total2

print("part2 :" +str(total2))