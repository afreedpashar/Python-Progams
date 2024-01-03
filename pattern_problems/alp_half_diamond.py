n = int(input("enter the n value: "))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()
for i in range(n-1):
    for j in range(n-i-1):
        print(chr(65+j),end=' ')
    print()


# output
# A 
# A B
# A B C
# A B C D
# A B C D E
# A B C D
# A B C
# A B
# A