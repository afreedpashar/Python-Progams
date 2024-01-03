l = ['hello',10,20,20,40,40,50,30,10]
d = []
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[i+1] and l[i] not in d:
            d.append(l[i])
print(d)
