n = int(input("enter the n value: "))
for i in range(n):
    print(" "*(n-i-1),end='')
    for j in range(i+1):
        print(chr(64+n-j),end=" ")
    print()


# enter the n value: 5 
#     E 
#    E D
#   E D C
#  E D C B
# E D C B A