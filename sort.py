a=list(map(int,input().split()))
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
for i in range(len(a)):
    print(a[i],end=', ')