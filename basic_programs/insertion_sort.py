def insert_sort(arr):
    for i in range(1,len(arr)):
        initial = arr[i]
        j = i-1
        while j>=0 and initial<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=initial

if __name__=='__main__':
    arr=[6,3,4,7,92,1]
    insert_sort(arr)
    print(arr)