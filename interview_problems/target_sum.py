# def target_sum(arr,ts):
#     a_len=len(arr)
#     if a_len<2:
#         print("No such pair")
#     for i in range(a_len):
#         for j in range(i+1,a_len):
#             if arr[i]+arr[j]==ts:
#                 print(arr[i],arr[j])
                

                
# ts=7
# arr=[4,5,6,8,1,2,7,12]
# (target_sum(arr,ts))
    
arr=[4,5,6,8,1,2,7,12]
ts = 9
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==ts:
            print(arr[i],"+",arr[j] ,"=",ts,"pair found at index", i,'and',j)
