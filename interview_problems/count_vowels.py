str1 = input("enter the string: ")
vowels ="a,e,i,o,u"
count=0
for ch in str1:
    if ch in vowels:
        count+=1
print(count)
