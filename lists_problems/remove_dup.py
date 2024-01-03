def remove_dup(li):
    no_dup=[]
    for i in li:
        if i not in no_dup:
            no_dup.append(i)
    return no_dup

li = [10,20,20,30,40,40,50,60]
print(remove_dup(li))