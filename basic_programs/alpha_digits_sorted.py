# Q9. Program to sort characters of the string, first alphabet symbols followed by digits

# s = "B4A1D3"
# alphabets = []
# digits = []

# for ch in s:
#     if ch.isalpha():
#         alphabets.append(ch)
#     else:
#         digits.append(ch)
# output = ''.join(sorted(alphabets)+sorted(digits))
# print(output)


s = "afreed"
output=" "
i = len(s)-1
while i>=0:
    output=output+s[i]
    i-=1
print(output)

# s = "learning python is easy"
# l = s.split()
# l1=l[::-1]
# output=" ".join(l1)
# print(output)

# s = "learning python is easy"
# l = s.split()
# l1=[]
# for words in l:
#     l1.append(words[::-1])
# output=" ".join(l1)
# print(output)
