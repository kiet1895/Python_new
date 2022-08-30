n='12'
c=4
a=list(n)
print(n,end=" ")
for i in range(c-1):
    m=0
    for i in a:
        m+=int(i)**2
    print(m,end=' ')
    a=list(str(m))