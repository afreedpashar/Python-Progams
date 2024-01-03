s = input("enter a string ")
n=len(s)
i=-1
temp = s
while i>=-n:
    rev = s[i]
    # print(rev,end="")
    i=i-1
if temp==rev:
    print("pallindrome")
else:
    print("not a pallindrome")