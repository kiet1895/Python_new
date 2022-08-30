# s = input()
import time
start=time.time()
s='80009081119'
d = [0] * 10
for i in range(10):
    d[i] = s.count(str(i))
le = 0
vt = 0
for i in range(10):
    if d[i] % 2 == 1: 
        le += 1
        vt = i
if le > 1: 
    print(0)
else:
    t = ""
    for i in range(1, 10):
        t += str(i) * (d[i] // 2)
        # print(t,str(i),(d[8] // 2))
    if t == "" and d[0] > 0: 
        print(0)
    else:
        if d[0] > 1: 
            t = t[0] + "0" * (d[0] // 2) + t[1:]
        if le == 1: 
            t +=  str(vt) + t[::-1]
        else: 
            t = t + t[::-1]
        print(t)
# end=time.time()
# print(f'time: {(end-start):.3f}')