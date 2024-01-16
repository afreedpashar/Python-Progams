# def second_largest_num(nums):
nums = [159,78,91,29,159,99]
f_lar = nums[0]
s_lar = nums[1]
for i in range(len(nums)):
    if nums[i]>f_lar:
        f_lar=nums[i]
for i in range(len(nums)):
    if nums[i]>s_lar and nums[i]!=f_lar:
        s_lar=nums[i]
print(s_lar)