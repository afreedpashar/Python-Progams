from collections import Counter
# def common(str1,str2):
#     dict1 = Counter(str1)
#     dict2 = Counter(str2)
#     commonDict = dict1 & dict2
#     if len(commonDict)==0:
#         print(-1)
#         return
#     commonChar = list(commonDict.elements())
#     commonChar = sorted(commonChar)
#     print(''.join(commonChar))
# str1 = "NAINA"
# str2 = "REENE"
# print(common(str1,str2))

def common(str1,str2):
    dict2=Counter(str1)
    dict1=Counter(str2)
    commonDict = dict1 & dict2
    if len(commonDict)==0:
        print(-1)
        return
    commonChar = list(commonDict.elements())
    commonChar=sorted(commonChar)
    print(''.join(commonChar))

str1 = "AFREED"
str2 = "NAWAZ"
print(common(str1,str2))