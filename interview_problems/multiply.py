var = input("enter two numbers:")
var = var.split()
num1,num2=var
result = 2
count =0
while True:
    result=result*2
    count+=1
    if result==num2:
        break
print(count)