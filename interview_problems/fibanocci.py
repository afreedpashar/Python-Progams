n = int(input("enter the number"))
for i in range(n):
    n1=0
    n2=1
    count=0
    if n<0:
        print("enter positive numbers")
    elif n==1:
        print(n1)
    else:
        print("fibonacci sequesnce: ")
        while n>count:
            print(n1)
            nth = n1+n2
            n1=n2
            n2=nth
            count+=1

