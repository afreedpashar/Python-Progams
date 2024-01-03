# list1 = [1,2,3,[1,[[2,4,5],6,7],7,8,[1,2,34]]] 
# list2 = [item for items in list1 for item in items]
# print(list2)


def flat(lis):
    flat_list = []
    for element in lis:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

lis = [1,2,3,[1,[[2,4,5],6,7],7,8,[1,2,34]]]
print(flat(lis))
