# s = input("Enter any string: ")

# i = 0
# for x in s:
#     print("The character at positive index {} and at negative index is {} is {}".format(i,i-len(s),x))
#     i=i+1

# s = ("learning python is not that easy")
# n = len(s)

# i=0
# print("forward direction")
# while n>i:
#     print(s[i],end="")
#     i=i+1

# print("backword direction")
# i=-1
# while i>=-n:
#     print(s[i],end="")
#     i=i-1

# s = ("what are you doing", "i am going to dubai")
# l = ','.join(s)
# print(l)

# st = ("I am learning python")
# print(st.upper())
# print(st.lower())
# print(st.swapcase())
# print(st.title())
# print(st.capitalize())

# program to reverse a string
# s = input("Enetr a string ")
# n = len(s)
# i = -1
# while i>=-n:
#     print(s[i],end="")
#     i=i-1

#program to reverse order of words

# s = input("enter any string: ")
# l=s.split()
# l1=[]
# i=len(l)-1
# while i>=0:
#     l1.append(l[i])
#     i=i-1
# output = ' '.join(l1)
# print(output,end="")    

#progarm to reverse ech internal content of word ina string

# s = input("enter any string: ")
# l=s.split()
# l1=[]
# i=0
# while len(l)>i:
#     l1.append(l[i][::-1])
#     i=i+1
# output=' '.join(l1)
# print(output)

#to print characters at even and odd position
# s = input("enter any string ")
# n = len(s)
# i=0
# print("characters at even position are")
# while n>i:
#     print(s[i],end=',')
#     i=i+2
# print()
# print("character at odd position are: ")
# i=1
# while n>i:
#     print(s[i],end='')
#     i=i+2

#merge characters of two strings alternatively

# s1=input("enter a string s1: ")
# s2 = input("enter a string s2: ")
# output=""
# i,j=0,0
# while len(s1)>i or len(s2)>j:
#     if len(s1)>i:
#         output=output+s1[i]
#         i=i+1
#     if len(s2)>j:
#         output=output+s2[j]
#         j=j+1
# print(output)

#program to check occurence of characters in a given string

# s = input("enter a string: ")
# d={}
# for x in s:
#     if x in d.keys():
#         d[x]=d[x]+1
#     else:
#         d[x]=1
# for k,v in d.items():
#     print("{}={} times".format(k,v))

#2nd way
# s=input("enter a string: ")
# for i in s:
#     print(i,"=",s.count(i),'times')


#to remove duplicates in a given string

# s = input("enter a string: ")
# output = ""
# for ch in s:
#     if ch not in output:
#         output=output+ch
# print(output)

def string_format(s):
    l = []
    temp = s.split('_')
    for i in temp:
        l.append(i[0].lower()+i[1:].upper())
    s='.'.join(l)
    print(s)
s = "I_am_a_Coder"
string_format(s)


