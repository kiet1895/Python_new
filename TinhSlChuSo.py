import time
start_time=time.time()
n='2 3 12 3 4 5 4 3 2 1'
s=list(map(int,n.split()))
a= [0]*(max(s)+1)
for i in range(min(s),len(a)):
    a[i]=s.count(i)
    if a[i]>0:
        print(f'có {a[i]} chữ số {i}')
end_time=time.time()
elapsed_time=end_time-start_time
print(f'time: {elapsed_time:.3f}')