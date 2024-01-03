# for i in range(1,1001):
#     num=i
#     n = len(str(i))
#     sum1=0
#     i=str(i)
#     for digit in i:
#         sum1=sum1+int(digit)**n
#     if sum1==num:
#         print(num)
    
#using while loop
        
for i in range(1,1001):
    num = i
    sum1 =0
    n = len(str(i))
    while (i!=0):
        digit=i%10
        sum1=sum1+digit**n
        i=i//10
    if sum1==num:
        print(num)

        
