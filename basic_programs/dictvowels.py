word = input("enter a word : ")
vowels = {'a','e','i','o','u'}
d = {}
for letr in word:
    if letr in vowels:
        d[letr] = d.get(letr,0)+1
for k,v in d.items():
    print(k, "occured", v, "times")
