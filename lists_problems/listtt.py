# n = [1,2,3,4,5,6,7,8,9]
# i=0
# while len(n)>i:
#     print(n[i])
#     i=i+1

# for number in n:
#     print(number)

#to print all the numbers divisible by 10 till 100

# l = []
# for i in range(101):
#     if i%10==0:
#         l.append(i)
# print(l)

#to print in matrix of a list
# n = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(n)):
#     for j in range(len(n[i])):
#         print(n[i][j],end=" ")
#     print()

#to print first letter of words in a list

# li = ['Sufiyan',"Afreed","Rayan","Ayan"]
# first = [w[0] for w in li]
# print(first)

# lis = ["nizam","nayeem","sheru","tannu"]
# mew_lis = [w[0] for w in lis]
# print(mew_lis)

vowels = ['a','e','i','o','u']
sentence = input("enter any string : ")

found = []
for vowel_letters in sentence:
    if vowel_letters in vowels:
        if vowel_letters not in found:
            found.append(vowel_letters)
print(found)
print(len(found))
