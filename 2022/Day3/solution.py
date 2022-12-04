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
print(elves)
first = []
second = []
common = []
value = dict(zip(string.ascii_lowercase, range(1,27)))
upper = dict(zip(string.ascii_uppercase, range(27,53)))
value.update(upper)
print(value)
# for x, y in zip(string.ascii_lowercase, range(1,27)):
#     print(x, y)
for n in elves:
    count = len(n)
    fir = n[slice(0, count//2)]
    sec = n[slice(count//2, count)]
    first.append(fir)
    second.append(sec)
    print(fir)
    print(sec)
    #compare and get common char
    a = list(set(fir)&set(sec))
    for i in a:
        common.append(i)        
    #add value

total = 0
for n in common:
    print(n)
    print(value[n])
    total = total + value[n]
#part1
print("Part1: " +str(total))

#part 2
common=[]
for i in range(0, len(elves), 3):
    a, b, c = elves[i:i+3]
    same = (set(a) & set(b) & set(c)).pop()
    common.append(same)

total = 0
for n in common:
    print(n)
    print(value[n])
    total = total + value[n]
#part1
print("Part2: " +str(total))