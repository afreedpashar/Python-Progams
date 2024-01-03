name = input("enter the string: ")
r_name = ""
i = len(name)
while i>0:
    r_name=r_name+name[i-1]
    i=i-1
print(r_name)