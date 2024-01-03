#python program to swap two elements

def swap_position(lis,pos1,pos2):
    temp = lis[pos1]
    lis[pos1] = lis[pos2]
    lis[pos2] = temp
    return lis
lis = [12,23,34,45,56]
pos1 = 0
pos2 = 3
print(swap_position(lis,pos1,pos2))

# orr

def swap_elements(lis,pos1,pos2):
    lis[pos1],lis[pos2] = lis[pos2],lis[pos1]
    return lis

lis = [10,22,33,44,55,66]
pos1 ,pos2 = 0,5
print(swap_elements(lis,pos1,pos2))

