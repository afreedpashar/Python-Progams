#ow to count unique elements present in a list

li = [1,2,2,3,4,5,6,6,7,7,8,8]
count = 0
res = []
for i in li:
    if i not in res:
        count+=1
        res.append(i)
print(count)
print(res)