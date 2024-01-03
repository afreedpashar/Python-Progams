from functools import *
l = [20,30,40,50,60]
l1 = reduce(lambda x,y:x+y,l)
l2 = reduce(lambda x,y:x*y,l)

print(l1)
print(l2)