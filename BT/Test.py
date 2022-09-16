# i=input()
# i='t'
# a=''
# for n in range (len(i)):
#     a=i[n]+a
# if a==i :
#     print ('YES')
# else:
#     print ('NO')


# n=str(input())
# s='aabce'
# s=list(n)
# a=list(set(s))
# kq=0
# for i in range(len(a)):
#     b=s.count(a[i])
#     if b%2!=0: 
#         kq=kq+1
# if kq!=0: 
#     kq=kq-1
# print(kq)
# s=input()
# a="abcdefghijklmnopqrstuvwxyz"
# d=0
# for i in a:
#       x = s.count(i)
#       if x % 2 == 1:
#           d += 1
# if d == 0:
#     print("0")
# else:
#     print(d-1)

# a = [1, 2, 3, 4, 5,6]
# [print(*a) for i in a]

# mylist = ["1", "2", "3","4", "5",'6']
# l=len(mylist)
# mylist[l//2:l//2] = ["a", "b"]
# l=len(mylist)
# mylist[l//2:l//2] = ["c", "d"]

# print(mylist)

# T = int(input())
# T=10
# for i in range(1, 11):
#     T = T + T*0.05
#     print(f'{T:.{3}f}')
#     print(format(T,'0.3f'))
# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# n=7;x=6
# a=[1,2,4,3,4,5,3]
# d=[0]*(max(a)+1)
# dem=0
# for i in a:
#     if i<x:
#         dem+=d[x-i]
#         d[i]+=1 
        
# d = {}
# ans = 0
# for i in a:
# 	j = x - i
# 	if j in d:
# 		ans = ans + d[j]
# 	if i in d:
# 		d[i] = d[i] +1
# 	else:
# 		d[i] = 1
# print(ans)
# n,b=map(int,input().split())
n=8;b=2
# a=list(map(int,input().split()))
a=[8 ,4 ,2 ,1 ,1 ,3 ,7 ,9]
a.sort(reverse=True)
ans=(a[0])
h=0
for i in range(1,n):
    if a[i]+b <= a[h]:
        h += 1
    else:
        ans += a[i]
print(ans)



