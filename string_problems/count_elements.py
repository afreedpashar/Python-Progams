a = [1,1,1,3,3,4,4,55,6,6,6]
count={}
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count,end="")