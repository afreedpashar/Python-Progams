# Python – List product excluding duplicates

#naive approach

# def prod(val):
#     res = 1
#     for ele in val:
#         res*=ele
#     return res

# test_list = [2,3,4,6,4,3,6,8,9,6]

# res = []
# for ele in test_list:
#     if ele not in res:
#         res.append(ele)
# res = prod(res)
# print(str(res))


#using list comprehension

def prod(val):
    res = 1
    for ele in val:
        res*=ele
    return res

new_list = [2,3,4,5,6,5,4,3,2]
res =[]
[res.append(i) for i in new_list if i not in res]
res=prod(res)
print(str(res))

