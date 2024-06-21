#sum of array elements
def sumof(a):
    b=0
    for i in a:
        b=b+i
    return b



a=list(map(int,input().split()))
print(sumof(a))