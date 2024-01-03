#Python – Convert Lists of List to Dictionary

li = [['a','b',1,2],['c','d',3,4],['e','f',5,6]]
res = dict()
for ele in li:
    res[tuple(ele[:2])] = tuple(ele[2:])
print(str(res))


#using dictionary comprehensions

li = [['a','b',1,2],['c','d',3,4],['e','f',5,6]]
res = {tuple(ele[:2]):tuple(ele[2:]) for ele in li}
print(str(res))


