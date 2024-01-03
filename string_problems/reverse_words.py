str1 = input("enter a string: ")
mylist=str1.split()
mylist=mylist[::-1]
str2=" ".join(mylist)
print(str2)