#to convert striing of integers to list it should be sorted
li = ['5','4','3','1','2']
res = [int(i) for i in li]
s = sorted(res)
print(s)

#to convert list of integers into list of string
li_int = [1,3,4,4,5,5,6,6]
res = [str(x) for x in li_int]
print(res)

