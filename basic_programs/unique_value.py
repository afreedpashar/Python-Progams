def unique_value(arr):
    lst = []
    count = 0
    for i in arr:
        if i not in lst:
            lst.append(i)
            count+=1
    return lst 
arr = [1,1,2,3,4,5,6,6,7,8,9,9]
print(unique_value(arr))