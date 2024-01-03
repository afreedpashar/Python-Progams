# def bubble_sort(arr):
#     n = len(arr)

#     # Traverse through all array elements
#     for i in range(n):
#         # Flag to optimize the loop (no swaps means the list is already sorted)
#         swapped = False

#         # Last i elements are already in place, so we don't need to check them
#         for j in range(0, n - i - 1):
#             # Swap if the element found is greater than the next element
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap the elements
#                 swapped = True

#         # If no two elements were swapped in the inner loop, the list is already sorted
#         if not swapped:
#             break

# # Example usage:
# arr = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(arr)
# print("Sorted array is:", arr)

def bub_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
arr=[12,34,6,7,11,5,10]
bub_sort(arr)
print(arr)