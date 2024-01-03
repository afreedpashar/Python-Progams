inp = int(input("enter a number: "))
temp = inp
s = 0
while temp>0:
    digit = temp%10
    s=s+digit**3
    temp=temp//10
if inp==s:
    print("armstrong number")
else:
    print("not armtrong")