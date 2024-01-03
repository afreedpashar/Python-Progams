def max_num(nums):
    max_num=nums[0]
    for i in nums:
        if i>max_num:
            max_num=i
    return max_num
nums=[45,78,12,46,98,66]
print(max_num(nums))


def min_num(nums):
    min_num=nums[0]
    for i in nums:
        if i<min_num:
            min_num=i
    return min_num
print(min_num(nums))