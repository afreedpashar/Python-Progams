n = int(input("enter n value: "))
for i in range(n):
    print(' '*(n-i-1)+(str(i+1)+" ")*(i+1))


#    1 
#   2 2
#  3 3 3
# 4 4 4 4


""" to find spaces we use (n-i-1) 
to print which symbol to print we have use the formula (i+1)
to print how many times we want to print this we use the same formula (i+1) 
"""