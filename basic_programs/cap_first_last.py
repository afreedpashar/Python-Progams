s = input("enter a string: ")
a=s.split()
res = []
for ch in a:
    x = ch[0].upper()+ch[1:-1]+ch[-1].upper()
    res.append(x)
output = ' '.join(res)
print(output)


