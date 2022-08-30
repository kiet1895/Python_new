# a,b= map(int,input().split())
# while m != n:
#     if m>n: m=m-n
#     else: n=n-m
# print(m)
a=36
b=42
while (a*b != 0): 
    if (a>b):
        a=a%b
    else:
        b=b%a
if a!=0:
    print(a)
else:
    print(b)