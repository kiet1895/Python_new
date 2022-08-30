# a = int(input())
# b = int(input())
a= 4
b=10
a += (3 - a % 3)%3
b -= b % 3
print((b - a)//3+1)
