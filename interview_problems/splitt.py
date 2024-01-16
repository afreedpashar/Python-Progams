num = 1235
temp = num
output = [int(x) for x in str(num)]
print(output)
summ = 0
for i in output:
    summ+=i
print(temp+summ)

