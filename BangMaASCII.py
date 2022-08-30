s='97122'
i=0
while i<len(s):
    if s[i]=='9':
        print(chr(int(s[i]+s[i+1])),end="")
        i+=2
    else:
        print(chr(int(s[i]+s[i+1]+s[i+2])),end='')
        i+=3
