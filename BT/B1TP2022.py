# n= int(input())
# k= int(input())
n = 9876543456
k = 4
socuoi=n- n%k
x= ((socuoi-1)//k)+1
print(((k+socuoi)*((socuoi-k)//k+1)//2))
# n = n - n%k