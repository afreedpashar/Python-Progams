# #merge sort for unsorted arrays

# def two_unsorted_arrays(a,b):
#     len_a=len(a)
#     len_b=len(b)
#     sorted_array=[]
#     i,j=0,0

#     while i<len_a and j < len_b:
#         if a[i] < b[i]:
#             sorted_array.append(a[i])
#             i+=1
#         else:
#             sorted_array.append(b[j])
#             j+=1

#     while i< len_a:
#         sorted_array.append(a[i])
#         i+=1
    
#     while j< len_b:
#         sorted_array.append(b[j])
#         i+=1
    
#     return sorted_array

# a = [2,67,23,45,56]
# b=[12,34,55,67]
# print(two_unsorted_arrays(a,b))

            
#optimized merge sort algorithm

def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i=j=k=0
        
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        
        while i<len(left):
            arr[k] = left[i]
            i+=1
            k+=1

        while j<len(right):
            arr[k] = right[j]
            j+=1
            k+=1
arr=[5,4,7,12,45,6,3,2]
merge_sort(arr)
print("Sorted array is",arr)