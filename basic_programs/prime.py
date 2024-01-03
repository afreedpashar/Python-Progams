num = int(input("Enter a number : "))
if num == 1:
    print("enter a number greater than 1")
if num>1:
    for i in range(2,num):
        if num%i!=0:
            print(num,"is prime number")
            break
        else:
            print(num," is not a prime number")
            break
