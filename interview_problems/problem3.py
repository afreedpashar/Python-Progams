str1 = "aaaabbbcccd"
char = str1[0]
count =0
output = ""
for ch in str1:
    if ch == char:
        count+=1
    else:
        output=output+str(count)+char
        count=1
        char=ch
output=output+str(count)+char
print(output)

# output 4a3b3c1d

