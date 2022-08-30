# x = int(input())
x= 9
if x % 2 == 0:
    x /= 2
    n = int(x / 2)
    if x % 2 == 0:
        print(n,n)
    else:
        print(n,n+1)
else:
    print(-1)