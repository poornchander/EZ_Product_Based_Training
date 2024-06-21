#for a given number n find out xor of all n numbers
a=int(input())
b=0
for i in range(a+1):
    b=b^i
print(b)

