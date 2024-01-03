#program to filter only even numbers usim=ng filter function

# def isEven(x):
#     if x%2==0:
#         return True
#     else:
#         return False
# l = [10,15,20,25,30,35,40,43,50,60]
# l1 = list(filter(isEven,l))
# print(l1)

#odd numbers filter
def isOdd(x):
    if x%2==0:
        return False
    else:
        return True
l = [3,4,6,8,10,20,15,21]
l1 = list(filter(isOdd,l))
print(l1)