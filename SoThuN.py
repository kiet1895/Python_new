# n=int(input())
n=5000003
if n<5000000:
    A=[]
    x=1
    while len(A)<n:
        if x%2==0 or x%3==0:
            A.append(x)
        x+=1
    print(A[n-1])
else:
    #Nhận xét 1 đoạn 6 số liên tục lấy 4 số
    A=[0,2,3,4]
    sd=n//4
    sc=sd*6
    print(sc+A[n%4])