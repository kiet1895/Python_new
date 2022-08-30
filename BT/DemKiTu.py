s=input()
dem=0
for i in range(len(s)):
    b=0
    b=s.count(s[i])
    if b==1:
        dem+=1
print(dem)
    