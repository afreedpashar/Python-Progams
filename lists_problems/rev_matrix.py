#reverse row sort list in lists of list

test_list = [[4,6,1],[78,12,55],[6,9,10]]
# for ele in test_list:
#     ele.sort(reverse=False)
# print(test_list)

#using list comprehensions

result = [sorted(ele,reverse=True) for ele in test_list]
print(str(result))

#if reverse = False we will get the matrix in sorted order