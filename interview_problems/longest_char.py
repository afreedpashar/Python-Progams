def long_char(s):
    charSet=set()
    l,r=0,0
    maxStr = 0
    maxL,maxR=0,0
    n=len(s)
    while r<n:
        if s[r] not in charSet:
            charSet.add(s[r])
            if r-l+1>maxStr:
                maxStr=r-l+1
                maxL=l
                maxR=r
            r+=1
        else:
            charSet.remove(s[l])
            l+=1
    return (s[maxL:maxR+1])
s = "GEEKFORGEEKS"
print(long_char(s))