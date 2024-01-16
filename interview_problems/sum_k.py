def maxOperations(nums, k):
        nums.sort()
        l , r = 0,len(nums)-1
        count = 0
        while l<r:
            if nums[l]+nums[r]==k:
                count+=1
                l+=1
                r-=1
            elif((nums[l]+nums[r]<k)):
                 l+=1
            else:
                 r-=1
        return count
nums = [3,1,3,4,3]
k =6
print(maxOperations(nums,k))

# nums = [1,12,-5,-6,50]
# summ = 0
# for i in nums:
#     summ+=i
# print(summ)
