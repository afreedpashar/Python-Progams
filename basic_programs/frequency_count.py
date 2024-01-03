inp =[1,2,3,3,4,5,5,6,6,7,7]
count = {}
for i in inp:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
print(count)