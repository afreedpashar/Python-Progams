#program to find the sum of values

# d = eval(input("enter a dictionary: "))
# s = sum(d.values())
# print(s)

#program to find the character occurence
word = input("enter a word: ")
d = {}
for x in word:
    d[x] = d.get(x,0)+1
for k,v in d.items():
    print(k, "occured", v, "times")