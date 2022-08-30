# # n=int(input())
# # m=int(input())




m=1
n=1000
dem=0
for i in range(m,n+1,1):
    # print(i)
    tong=0
    for k in range(1,(i//2)+1):
        if i%k==0:
            tong+=k
    if tong>i:
        dem+=1
        print(i)
print(dem)

