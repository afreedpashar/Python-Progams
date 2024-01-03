#program to double the the elements of a list
# l =[2,3,45,5,6,7]
# l1 = list(map(lambda x:x*2,l)) 
# print(l1)

l1 = [2,3,4,5,6]
l2 = [3,4,5,6,7]
l3 = list(map(lambda x,y:x+y,l1,l2))
l4 = list(map(lambda x,y:x*y,l1,l2))
l4 = list(map(lambda x,y:x*y,l1,l2))
l5 = list(map(lambda x,y:x/y,l1,l2))


print(l3)
print(l4)
print(l5)
