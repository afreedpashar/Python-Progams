mylist=[1,2,2,3,34,5,5,5,6,6]
# new_list=[]
# for i in mylist:
#     if mylist.count(i)==1:
#         new_list.append(i)
# print(new_list)

'''by using list comprehension'''
print([i for i in mylist if mylist.count(i)==1])