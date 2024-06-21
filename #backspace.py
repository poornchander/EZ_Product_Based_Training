s=input()
t=input()
c=[]
d=[]
for i in range(len(s)):
    c.append(s[i])
    for j in range(len(c)):
        if c[j]=="#":
            c.pop()
            c.pop()
            

for i in range(len(t)):
    d.append(t[i])
    for j in range(len(d)):
        if d[j]=="#":
            d.pop()
            d.pop()
            
print(c,d)

if c==d:
    print(True)
else:
    print(False)
            
            

        