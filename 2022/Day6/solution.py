f= open('input.txt', 'r').read()

def get_char_count(part,n):
    i=0
    for i in range(0,len(f)):
        marker = f[i:i+n]
        if len(set(marker)) == n:
            break
    return print("Part " +str(part)+": "+str(i+n))

#part1
get_char_count(1, 4)
#part2
get_char_count(2, 14)