#search element in array   
def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return False

arr=list(map(int,input().split()))
x=int(input())
print(search(arr,x))