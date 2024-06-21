def findsingle(ar,n):
    res=ar[0]
    for i in range(1,n):
        res=res^ar[i]
    return res

ar=[2,3,5,4,5,3,4,2,88]
print(findsingle(ar,len(ar)))