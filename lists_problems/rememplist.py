#remove empty list form list using list comprehension
# li = [2,3,4,[],5,[],7,8,[]]
# res = [ele for ele in li if ele!=[]]
# print("after removing empty lists in list",str(res))

#using filter method 

# li = [2,3,4,[],5,[],7,8,[]]
# res = list(filter(None,li))
# print(res)

# naive method
li = [2,3,4,[],5,[],7,8,[]]
res = []
for ele in li:
    if ele != []:
        res.append(ele)
print(str(res))
