str1 = input("enter the string : ")
upper_case=""
for ch in str1:
    asc=ord(ch)
    if asc>64 and asc<91:
        upper_case=upper_case+chr(asc+32)
    else:
        upper_case=upper_case+chr(asc)
print(upper_case)
