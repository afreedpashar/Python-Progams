def pushZeroes(arr):
    n = len(arr)
    j =0
    for i in range(n):
        if arr[i]!=0:
            arr[j],arr[i]=arr[i],arr[j]
            j+=1
    return arr
arr=[1,2,0,0,3,4,0,3,5]
print(pushZeroes(arr))