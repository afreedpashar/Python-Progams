def ele_count(s):
    res ={}
    for i in s:
        if i in res:
            res[i]+=1
        else:
            res[i]=1
    return res
s = "afreed"
print(ele_count(s))