# def flat(lis):
#     flatlist=[]
#     for element in lis:
#         if type(element) is list:
#             for item in element:
#                 flatlist.append(item)
#         else:
#             flatlist.append(element)
#     return flatlist

lis = [[1,2,3],4,5,[9,78,22],[22,45]]
# print(flat(lis))

# or list comprehension 

li = [element for innerlist in lis for element in innerlist]
print(li)