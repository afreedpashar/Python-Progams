# string = a3b5c4
# output = aaabbbbbcccc

str1 = input("enter a string: ")
output=""
for ch in str1:
    if ch.isalpha():
        var=ch
    else:
        num=int(ch)
        output=output+(var*num)
print(output)