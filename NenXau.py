s='mmaabbbeeeezh'
i=0
d=0
# while i < len(s):
#     x=s.count(s[i])
#     if x==1:
#         print(s[i],sep='',end='')
#     else:
#         print(x,s[i],sep='',end='')
#     i+=x
a=list(s); x= set(a)
for i in x:
    # print(i)
    d=s.count(i)
    if d==1:
        print(i,sep='',end='')
    else:
        print(d,i,sep='',end='')