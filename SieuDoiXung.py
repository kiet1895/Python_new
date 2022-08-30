# # a=input()
# from re import I


# a='15'
# b=len(a)*'1'
# c= int(a)%int(b)
# print (round(int(b)-int(a)%int(b)))
# n = int(input())
'''''
n='876543987665477'
# a=int(str(n)[0] * len(str(n)))

# if int(str(n)[0] * len(str(n))) > n:
#     print(int(str(n)[0] * len(str(n))) - n)
# else:
#     print('d')
#     if int(str(n)[0]) + 1 != 10:
#         print("x")
#         print(int(str(int(str(n)[0]) + 1) * len(str(n))) -n )
#     else:
#         print('c')
#         print(int('1' * (len(str(n)) + 1)) - n)
if int(n[0]<n[1]):
    a=int(n[0])+1
    a=str(a)*len(n)
elif int(n[0]==n[1]):
    if int(n[0])==9:
        a=str(1)*(len(n)+1)
    else:
        a=str((int(n[0])+1))*len(n)
else:
    a=n[0]
    a=str(a)*len(n)
    # for i in range(1,len(n)):
    #     a+=n[0]
print(int(a)-int(n))
'''''




a=input()
if a.count('9')==len(a):
    b=(len(a)+1)*'1'
else :
    b=len(a)*'1'
print (int(b)-int(a)%int(b))