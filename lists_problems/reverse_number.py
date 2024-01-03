def rev(num):
    reversed_num = 0
    while num>0:
        last_digit = num%10
        reversed_num = reversed_num*10 + last_digit
        num = num//10
    return reversed_num

number = int(input("enter a number: "))
print('the reversed number is',rev(number))