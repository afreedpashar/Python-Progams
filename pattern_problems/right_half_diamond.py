n = int(input("enter tehe value of n:"))
for i in range(n):
    print("* "*(i+1))
for i in range(n-1):
    print("* "*(n-i-1))

# output
# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *