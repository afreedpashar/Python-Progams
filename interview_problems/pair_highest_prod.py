def highest_prod_pair(arr):
    arr_len = len(arr)
    if arr_len<2:
        print("No such pair")
    a = arr[0]
    b = arr[1]
    for i in range(arr_len):
        for j in range(i+1,arr_len):
            if (arr[i]*arr[j])>(a*b):
                a=arr[i]
                b=arr[j]
    return a,b


arr = eval(input("enter an array: "))
print(highest_prod_pair(arr))