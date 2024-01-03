def max_freq(s):
    res ={}
    for i in s:
        if i in res:
            res[i]+=1
        else:
            res[i]=1
        ans = max(res,key=res.get)
    return ans
s="geeksforgeeks"
print(max_freq(s))