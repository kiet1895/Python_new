n,m,k=list(map(int,input().split()))
s2=[]
for i in range(1,n+1):
    for x in range(1,m+1):
        s2.append(i*x)
s2.sort()
print(s2[k-1])