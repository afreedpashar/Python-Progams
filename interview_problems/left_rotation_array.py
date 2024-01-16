# def printArray(arr):
#     for i in range(len(arr)):
#         print(arr[i],end='')

def leftRotation(arr,shift):
    for i in range(0,shift):
        temp = arr[0]
        for j in range(0,len(arr)-1):
            arr[j] = arr[j+1]
        arr[len(arr)-1] = temp
    return arr


arr = [1,2,3,4,5,6]
shift = 3
print(leftRotation(arr,shift))