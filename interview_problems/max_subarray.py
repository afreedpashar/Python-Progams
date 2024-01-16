def maxSubArray(nums,k):
    s = nums[:k]
    sum1 = 0
    for i in s:
        sum1+=i
    maxSum=sum1
    start_index = 0
    end_index = k
    n = len(nums)
    while(end_index<n):
        sum1-=nums[start_index]
        start_index+=1
        sum1+=nums[end_index]
        end_index+=1
        maxSum=max(maxSum,sum1)
    return float(maxSum/k)
nums=[1,3,12,-5,-6,-50,3]
k=3
print(maxSubArray(nums,k))