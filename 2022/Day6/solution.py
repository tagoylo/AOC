import re          

def split_on_empty_lines(s):

    blank_line = r"(?:\r?\n){2,}"
    two_blank_line = r"(?:\r?\n){3,}"
    new_line = r"\r\n|\r|\n"
    character = r"[a]"

    return re.split(new_line, s.strip())

f= open('input.txt', 'r').read()
#elves=split_on_empty_lines(f)
#print(f)

i=0
for i in range(0,len(f)):
    start = i
    end = i+4
    marker = f[start:end]
    #print(marker)
    if len(set(marker)) == 4:
        #print(marker[-1:])
        print("Part1: "+str(end))
        break

i=0
for i in range(0,len(f)):
    start = i
    end = i+14
    marker = f[start:end]
    #print(marker)
    if len(set(marker)) == 14:
        #print(marker[-1:])
        print("Part2: "+str(end))
        break