inp="AC*wv12n/:e123we2.45oin (fwoi6n#a98nfwb+owi"
temp=""
data=[]
for ch in inp:
    if ch.isdigit() or (ch=='.' and '.' not in temp):
        temp=temp+ch
    elif len(temp)!=0:
        data.append(eval(temp))
        temp=""
data.sort()
print(data)
