n = int(input("enter the value of n: "))
for i in range(n):
    print(" "*i,end="")
    for j in range(n-i):
        print(chr(65+j), end=" ")
    print()


# output
# enter the value of n: 5
# A B C D E 
#  A B C D
#   A B C
#    A B
#     A

for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()

#     A 
#    A B
#   A B C
#  A B C D
# A B C D E