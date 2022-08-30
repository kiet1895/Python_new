# n=input()
# lenh=input()
"""""
n="abcde"
lenh="RRRR"
LenhR=lenh.count('R')
LenhL=lenh.count('L')
for i in lenh:
    if i == 'L':
        # n=n[1:len(n)]+n[0]
        n=n[1:]+n[0]
    else:
        # n=n[len(n)-1]+n[0:len(n)-1]
        n=n[-1:-2:-1]+n[:-1]
print (n)"""""
# ---------------------------------------------------------------
n="abcde"
# lenh="RLRR"
# LenhR=lenh.count('R')
# LenhL=lenh.count('L')
LenhR=15
LenhL=18
if LenhR > LenhL:
    m=LenhR-LenhL
    x=m%len(n)
    n=n[-x:]+n[:-x]
else:
    m=LenhL-LenhR
    x=m%len(n)
    n=n[x:]+n[:x]
    
    
if LenhR == LenhL:
    m=LenhR-LenhL
# if LenhR !=0:
#     n=n[-LenhR:]+n[0:-3]
# # if LenhL!=0:
# #     n=n[LenhL+0:]+n[0:LenhL]
print(n)