# input = ACB6487
# output=ABC4678

str1= input("enter the string:")
alphabets = []
numbers =[]
for ch in str1:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        numbers.append(ch)
new_li = sorted(alphabets)+sorted(numbers)
output = "".join(new_li)
print(output)