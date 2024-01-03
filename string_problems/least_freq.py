def least_freq(s):
    all_freq={}
    for i in s:
        if i in all_freq:
            all_freq[i]+=1
        else:
            all_freq[i]=1
    res = min(all_freq,key=all_freq.get)
    return res

s="geeksforgeeks"
print(least_freq(s))