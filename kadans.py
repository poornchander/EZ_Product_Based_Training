def kadanes(arr):
    _sum=float("-inf")
    cs=arr[0]
    n=len(arr)
    for i in range(1,n):
        if cs<0:
            cs=0
        if arr[i]<0:
            _sum=max(_sum,cs+arr[i])
        cs=cs+arr[i]
    return max(_sum,cs)

arr=[-2,-3,4,-1,-2,1,5,-3]
print(kadanes(arr))