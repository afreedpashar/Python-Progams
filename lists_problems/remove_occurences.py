# def remove_occ(li,item):
li = [1,1,1,2,3,4,45,1]
item = 1
# res = []
# for i in li:
#     if i != item:
#         res.append(i)
# print(str(res))

# item = 1
# li = [1,1,1,2,3,4,45,1]
# print(remove_occ(li,item))

#using list comprehensions

res = [i for i in li if i!=item]
print(res)