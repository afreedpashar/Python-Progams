# def missNum(arr,n):
#     total_sum = (n+1)*(n+2)/2
#     sum_of_arr = sum(arr)
#     total = total_sum-sum_of_arr
#     return total

# if __name__=='__main__':
#     arr = []
#     n = int(input("enter the len of an array: "))
#     for i in range(n):
#         m = int(input("Enter the numbers: "))
#         arr.append(m)

# print(missNum(arr,n))

def missNum(arr,n):
    total_sum = (n+1)*(n+2)//2
    expected_sum = sum(arr)
    total = total_sum-expected_sum
    return total

arr = [1,2,3,5]
n = len(arr)
print(missNum(arr,n))
