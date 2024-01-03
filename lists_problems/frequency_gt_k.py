#extract element with frequeny greater than k

test_list = [4,6,3,3,3,4,4,4,4,5,6,6,7,8 ]
# import pdb;pdb.set_trace()
k = 2
res = []
for i in test_list:
    freq = test_list.count(i)
    if freq>k and i not in res:
        res.append(i)

print(str(res))