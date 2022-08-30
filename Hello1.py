a='hello'
for i in range(int(input())):
    s=input()
    i=0
    for j in range(len(s)):
        if i==5: 
            break
        else:
            if s[j]==a[i]: 
                i+=1
    if i==5: 
        print ("YES")
    else: 
        print("NO")
