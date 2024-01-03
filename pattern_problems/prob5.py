n = int(input("enter the n value: "))
for i in range(n):
    print((chr(64+n-i)+" ")*n)

# output
# enter the n value: 5
# E E E E E 
# D D D D D
# C C C C C
# B B B B B
# A A A A A

for i in range(n):
    for j in range(n):
        print((n-j),end=" ")
    print()

# output
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1