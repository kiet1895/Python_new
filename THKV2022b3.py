n = 5
m = 10
k = 2
d = 0
t=n
while t< m:
    d+=1
    if d%2!=0:
        t+=k
        x=k
    else:
        t-=x//2
        if k==1:
            d+=(m-t)*2-1
            t=m
        else:
            k-=1