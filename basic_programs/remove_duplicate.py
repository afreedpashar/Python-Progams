# using string
s = input("enter a given string: ")
output = ''
for ch in s:
    if ch not in output:
        output+=ch
print(output)

# uisng list
s = input("enter a given string: ")
l = []
for ch in s:
    if ch not in l:
        l.append(ch)
output =''.join(l)
print(output)

# using set  
s = input("enter a given string: ")
s1 = set(s)
output = ''.join(s1)
print(output)
