#program to reverse a string:

# s = input("enter any string: ")
# n = len(s)
# i = -1
# while i>=-n:
#     print(s[i],end="")
#     i=i-1

s = input("Enter a string : ")
rev = ""
for i in s:
    rev=i+rev
print(rev)