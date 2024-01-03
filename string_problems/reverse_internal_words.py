s = input("enter a string: ")
li = s.split()
new_li=[]
for ch in li:
    new_li.append(ch[::-1])
output = " ".join(new_li)
print(output)