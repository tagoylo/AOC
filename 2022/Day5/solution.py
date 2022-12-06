import re
from unittest.util import three_way_cmp        


one = ['J', 'H', 'P', 'M', 'S', 'F', 'N', 'V']
two = ['S' ,'R' ,'L','M','J','D','Q']
three = ['N', 'Q' ,'D', 'H' ,'C', 'S','W' ,'B']
four = ['R','S','C','L']
five = ['M','V','T','P','F','B']
six = ['T','R','Q','N','C']
seven = ['G','V','R']
eight = ['C','Z','S','P','D','L','R']
nine =  ['D','S','J','V','G','P','B','F']

counter = {"1":one, "2":two, "3":three, "4":four, "5":five, "6":six, "7":seven, "8":eight, "9": nine}



def split_on_empty_lines(s):

    blank_line = r"(?:\r?\n){2,}"
    two_blank_line = r"(?:\r?\n){3,}"
    new_line = r"\r\n|\r|\n"
    character = r"[a]"

    return re.split(blank_line, s.strip())

f= open('input.txt', 'r').read()
items=split_on_empty_lines(f)
commands = items[1].split("\n") #commands

for command in commands:
    comm = command.split(" ")
    count =comm[1]
    #print(count)
    from_number =comm[3]
    #print(from_number)
    to_number =comm[5]
    #print(count)
    #print(counter[from_number])
    from_ = counter[from_number]
    #print(from_)
    to_ = counter[to_number]
    #print(from_)
    trans = []
    while int(count) > 0:
        trans.append(from_.pop())
        count = int(count) - 1
    #print(trans)
    for i in trans:
        to_.append(i)
    #print(to_)
print("PART1")
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)
print(nine)


    #get list from

one = ['J', 'H', 'P', 'M', 'S', 'F', 'N', 'V']
two = ['S' ,'R' ,'L','M','J','D','Q']
three = ['N', 'Q' ,'D', 'H' ,'C', 'S','W' ,'B']
four = ['R','S','C','L']
five = ['M','V','T','P','F','B']
six = ['T','R','Q','N','C']
seven = ['G','V','R']
eight = ['C','Z','S','P','D','L','R']
nine =  ['D','S','J','V','G','P','B','F']

counter = {"1":one, "2":two, "3":three, "4":four, "5":five, "6":six, "7":seven, "8":eight, "9": nine}  

for command in commands:
    comm = command.split(" ")
    count =comm[1]
    #print(count)
    from_number =comm[3]
    #print(from_number)
    to_number =comm[5]
    #print(count)
    #print(counter[from_number])
    from_ = counter[from_number]
    #print(from_)
    to_ = counter[to_number]
    #print(from_)
    trans = []
    trans_rev =[]
    trans = from_[-int(count):]
    trans_rev=trans[::-1]
    #print(trans_rev)
    #print(trans)
    for i in range(0, int(count)):
        from_.pop()
    # trans_rev = []
    # trans_rev.append(trans[::-1])
    #print(trans)
    #print(to_)
    for i in trans:
        to_.append(i)
    #print(to_)
print("PART2")
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)
print(nine)

