from itertools import count


n = int(input())
for i in range(n):
    x =0 
    y = 0
    a=input()
    x += a.count("E")
    x -= a.count("W")
    y += a.count("N")
    y -= a.count("S")
    print(x,y)