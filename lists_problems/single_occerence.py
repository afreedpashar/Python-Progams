li = [1,2,2,3,3,4,5,5,5,6,6]
count = 0
new_li=[]
for i in li:
    if i not in new_li:
        new_li.append(i)
        count+=1
print(new_li)