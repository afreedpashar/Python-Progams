#python program to interchange the first and last digit of a list

def swap(li):
    n = len(li) #to get the length of the list we can 
    temp = li[0] # here we store the first index value of list in a temp variable
    li[0] = li[n-1] #li[n-1] gives the last value of a list
    li[n-1] = temp
    return li
li = [12,13,45]
print(swap(li))