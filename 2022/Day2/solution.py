import re

def split_on_empty_lines(s):

    blank_line = r"(?:\r?\n){2,}"
    two_blank_line = r"(?:\r?\n){3,}"
    new_line = r"\r\n|\r|\n"
    character = r"[a]"

    return re.split(new_line, s.strip())

f= open('input.txt', 'r').read()
elves=split_on_empty_lines(f)

#print(elves)

score = { "X": 1, "Y": 2, "Z": 3}
total = 0
for n in elves:
    a = n.split()[0]
    b = n.split()[1]
    score_total=0
    if a == "A" and b == "X" or a == "B" and b == "Y" or a == "C" and b == "Z":
        #draw
        score_total = int(score[b]) + 3
    elif a == "A" and b == "Z" or a == "B" and b == "X" or a == "C" and b == "Y":
        #lose
        score_total = int(score[b])
    elif a == "A" and b == "Y" or a == "B" and b == "Z" or a == "C" and b == "X":
        #win
        score_total = int(score[b]) + 6
    total =total +score_total
#part 1
print("part1: " +str(total))


score_lose = {"A": 3, "B": 1, "C": 2}
score_win = {"A": 2, "B": 3, "C": 1}
score_draw = {"A": 1, "B": 2, "C": 3}
total2 = 0
for n in elves:
    a = n.split()[0]
    b = n.split()[1]
    score_total=0
    if a == "A" and b == "X" or a == "B" and b == "X" or a == "C" and b == "X":
        #lose
        score_total = int(score_lose[a])
    elif a == "A" and b == "Y" or a == "B" and b == "Y" or a == "C" and b == "Y":
        #draw
        score_total = int(score_draw[a]) + 3
    elif a == "A" and b == "Z" or a == "B" and b == "Z" or a == "C" and b == "Z":
        #win
        score_total = int(score_win[a]) + 6
    total2 =total2 +score_total
#part2
print("part2: "+str(total2))
