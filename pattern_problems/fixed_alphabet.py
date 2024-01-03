# A
# B B
# C C C 
# D D D D 
# E E E E E 

# Right angled triangle with fixed alphabets

n = int(input("enter n value: "))
for i in range(n):
    print((chr(65+i)+' ')*(i+1))
