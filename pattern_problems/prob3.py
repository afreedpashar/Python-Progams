n = int(input("enter  the n value:"))
for i in range(n):
    for j in range(n):
        print(str(j+1),end=" ")
    print()

# enter  the n value:4
# 1 2 3 4 
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

for i in range(n):
    for j in range(n):
        print(chr(65+j),end=" ")
    print()
    
# output
# A B C D
# A B C D
# A B C D
# A B C D