s = input("Enter the string: ")
n = int(input("Enter the count : "))
s = s.split()
new_li=[]
for i in s:
    if s.count(i)==n:
        new_li.append(i)
output =' '.join(new_li)
print(output)
