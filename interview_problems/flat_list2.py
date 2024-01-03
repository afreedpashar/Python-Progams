li = [1,2,3,[1,2,3],[5,5,6]]
#li = [1,2,3,1,2,3,5,5,6]
new_li=[]
for elements in li:
    if type(elements) is list:
        for digit in elements:
            new_li.append(digit)
    else:
        new_li.append(elements)
print(new_li)

