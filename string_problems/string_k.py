# Find words which are greater than given length k
# Input : str = "hello geeks for geeks 
#           is computer science portal" 
#         k = 4
# Output : hello geeks geeks computer 
#          science portal
# Explanation : The output is list of all 
# words that are of length more than k.

def string_k(k,s):
    res = []
    text = s.split(" ")
    for ele in text:
        if len(ele)>k:
            res.append(ele)
    return res
k=2
s="hey geeks for geeks"
print(string_k(k,s))

