#program to reverse internal content of string

#input = My name is Afreed
#output = yM eman si deerfA

s = input("Enter the string: ")
l=s.split()
l1 = []
i = 0
while len(l)>i:
    l1.append(l[i][::-1])
    i=i+1
output = ' '.join(l1)
print(output)