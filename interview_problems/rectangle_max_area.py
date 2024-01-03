def rectangle(ar):
    # n=len(arr)
    arr_new = []
    for num in arr:
        if arr.count(num)>=2 and num not in arr_new:
            arr_new.append(num)
    #to find max prod
    max_area= 0
    for i in range(len(arr_new)):
        for j in range(i+1,len(arr_new)):
            if arr_new[i]*arr_new[j]>max_area:
                max_area=arr_new[i]*arr_new[j]
    return max_area

# n =8
arr=[4,4,2,2,5,5,1,3,3]
print(rectangle(arr))
