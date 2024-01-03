def find_dup_char(inp):
    x = []
    for i in inp:
        if i not in x and inp.count(i)>1:
            x.append(i)
    print(" ".join(x))

inp = 'geeksforgeeks'
print(find_dup_char(inp))