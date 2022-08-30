# n = int(input())

# 1470369258 = 45

n = 804361624
tong = 0
# so = 1
# ------------------------------------------------------------
a= [1,4,7,0,3,6,9,2,5,8]
# print(len(a))
x = n%len(a)
y = n//len(a)
if n%10==0:
    tong = 45*y
else:
    for i in range(x):
        tong = tong + int(a[i])
    tong += 45*y
print(tong)
    



# for i in range(1,n+1):
#     x = str(so)[len(str(so))-1]
#     print(x)
#     so += 3
#     tong+=int(x)
