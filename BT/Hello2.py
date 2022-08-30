sl=int(input("sl:"))
s1=input("key: ")
for i in range(sl):
    s2=input()
    j=0
    dem=0
    for i in range(len(s2)):
        if j== len(s1):
            break
        else:
            if s1[j]==s2[i]:
                j+=1
                dem+=1
    if dem==len(s1):
        print('y')
    else:
        print('n')
        