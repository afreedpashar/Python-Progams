def returnSum(dict):
    import pdb;pdb.set_trace()
    sum = 0
    for i in dict.values():
        sum+=i
    return sum
dict = {'afreed':100,'tanveer':200,'rehman':300}
print(returnSum(dict))


listtt = ['11','22','33','3']
res = sorted([int(i) for i in listtt])
print(res)
