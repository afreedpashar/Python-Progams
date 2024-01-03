from functools import reduce
li = [2,3,4,5,6,7]


new_li = reduce(lambda x,y:x*y,li)
print(new_li)