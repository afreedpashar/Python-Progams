list_1 = [[1,2],[2,3],[4,5]]
list_2 = [[1,2],[5,60],[2,3]]

# res =[]
# for i in list_1:
#     if i not in list_2:
#         res.append(i)
# for i in list_2:
#     if i not in list_1:
#         res.append(i)
# print(str(res))

#using list comprehensions
res = [x for x in list_1 if x not in list_2] + [y for y in list_2 if y not in list_1]
print(res)
