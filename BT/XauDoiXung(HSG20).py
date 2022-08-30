n='aammmda'
s=list(n)
a=list(set(s))
kq=0
for i in range(len(a)):
    b=s.count(a[i])
    if b%2!=0: 
        kq=kq+1
if kq!=0: 
    kq=kq-1
print(kq)
