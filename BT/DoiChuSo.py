s='8000990811'
d=[0]*10
dem=0
t=''
for i in range(10):
    d[i]= s.count(str(i))
for i in range(len(d)):
    if d[i]%2!=0:
           dem+=1
           vt=i 
if dem>1:
    print('0')
else:
    for i in range(1,10):
        t+=str(i)*(d[i]//2)
    if t=='' and d[0]>0:
        print('0')
    else:
        if d[0]>1:
            print(t)
            t = t[0] + "0" * (d[0] // 2) + t[1:]
        if dem==1:
            t+=str(vt)+t[::-1]
        else:
            t+=t[::-1]
        print(t)
        