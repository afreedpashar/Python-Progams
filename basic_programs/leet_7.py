def rev_num(x):
    # import pdb;pdb.set_trace()
    MAX_INT = 2**31-1
    MIN_INT = -2**31
    reverse = 0

    while x!=0:
        if(reverse>MAX_INT/10 or reverse<MIN_INT/10):
            return 0
        digit=x%10 if x>0 else x%-10
        reverse=reverse*10+digit
        x=x//10
    return reverse

x = 1234
rev_num(x)
print(rev_num(x))