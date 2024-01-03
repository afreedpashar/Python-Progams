str1 = input("enter the string: ")
subs = []
count = 0
for i in range(0,len(str1)):
    for j in range(i+1,len(str1)+1):
        subs.append(str1[i:j])
        count+=1
print(subs)
print(f"Total number of substrings are {count}")