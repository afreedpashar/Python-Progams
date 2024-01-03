s = 'a4b2c5'
output = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output=output+x*d
print(output)

# s="aaaabbbcccdddw"
#output = 4a3b3c2d1w

# initial = s[0]
# i = 1
# count = 1
# output = ''
# while i < len(s):
#     if s[i]  == initial:
#         count+=1

#     else:
#         output =output+str(count)+initial
#         initial = s[i]
#         count = 1

#     if i == len(s)-1:
#         output=output+str(count)+initial
#     i=i+1

# print(output)

# s = "a4b3c3"
# output = ''
# for ch in s:
#     if ch.isalpha():
#         x = ch
#     else:
#         d = int(ch)
#         output=output+x*d
# print(output)

#input = a4k3b2
# output = aeknbd

# s="a4k3b2"
# output = ''
# for ch in s:
#     if ch.isalpha():
#         output=output+ch
#         x=ch
#     else:
#         d = int(ch)
#         new_char = chr(ord(x)+d)
#         output = output+new_char
# print(output)

