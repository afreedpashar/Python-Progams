num = int(input("enter the number: "))
num1=num
reverse=0
while num>0:
    digit=num%10
    reverse = reverse*10+digit
    num=num//10
if num1==reverse:
    print("Pallindrome")
else:
    print("Not a pallindrome")

