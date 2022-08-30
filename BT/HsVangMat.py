n,m= map(int,input().split())
x=list(map(int,input().split()))
d=[1]+[0]*n
for i in x:
    d[i]+=1
for i in range(len(d)):
    if d[i]<1:
        print(i,end=' ')