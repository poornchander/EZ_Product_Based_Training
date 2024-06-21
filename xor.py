#find the xor for the given range
a=int(input())
c=int(input())
b=0
for i in range(a,c+1):
    b=b^i
print(b)
