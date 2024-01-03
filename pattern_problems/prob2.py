n = int(input("enter the n value: "))
for i in range(n):
    print((str(i+1)+" ")*n)

# output
# enter the n value: 5
# 1 1 1 1 1 
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

for i in range(n):
    print((chr(65+i)+' ')*n)

# output
# A A A A A
# B B B B B
# C C C C C
# D D D D D
# E E E E E

