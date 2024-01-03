#using two pointer methods
def rev_list(arr):
    left = 0
    right = len(arr)-1
    for i in range(len(arr)):
        temp = arr[left]
        arr[left] =arr[right]
        arr[right]=temp
        left+=1
        right-=1
        return arr
arr=[1,2,3,4,5,6,7,8,9]
print(rev_list(arr))

        #or by using insert function

# lst = [1,2,3,4,5,6,7]
# l = []
# for i in lst:
#     l.insert(0,i)
# print(l)

# li=[1,2,3,4,5,56]
# new_li=[56,5,4,3,2,1]