s = ['110','20','40','50','70']
new_list=[]
for i in s:
    if type(i) == str:
        new_list.append(int(i))
    else:
        pass
print(new_list)    #use this method to convert str list of integers into a integer list


# from ast import literal_eval

# s = "['1','3','4','6,','8']"
# literal_eval(s)
# new_list=[]
# for i in s:
#     if type(i)==str:
#         new_list.append(int(i))
#     else:
#         pass
# print(new_list)
