from pickle import TRUE


# s='9990'
# a=[]
# tong=0
# for i in range(len(s)):
#     a.append(s[i])
# c = sorted(a,reverse= True)
# d= c[:len(c)-1]
# for i in range(len(d)):
#     tong+=int(d[i])
# if tong%3==0 and c[len(c)-1]=='0':
#     for i in range(len(c)):
#         print(c[i],end='')
# else:
#     print("-1")
s='102'
if s.count('0')>0:
    tong=0
    for i in range(len(s)-1):
        tong+=int(s[i])
    if tong%3==0:
        s=list(s)
        s.sort(reverse= True)
        print(''.join(s))
    else:
        print('-1')
else:
    print('-1')