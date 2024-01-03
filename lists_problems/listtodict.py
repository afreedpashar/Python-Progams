#python convert list into dictionary

li = ['Afreed',24,'Rehman',25,'Tanveer',26,'Nizam',24,'Nawaz',28]
key_li = ['Name','Age']
n = len(li)
res = []
for i in range(0,n,2):
    res.append({key_li[0]:li[i],key_li[1]:li[i+1]})
print(str(res))