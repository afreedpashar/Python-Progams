"""write a program in which take two inputs one is string and other a array of stringd if the length of first string is n and length of words
in array is n-1 and after removing a character from string check if it matches with any other word in an array
of string if presnt return the count"""

def equalization(n,m,s,t): 
    count =0
    s1=[]
    for ch in s:
        s1.append(ch)
    for i in range(n):
        char=s1.pop(i)
        j = "".join(s1)
        for word in t:
            if j==word:
                count+=1
        s1.insert(i,char)
    return count
n = 5
m = 4
s="abcdc"
t=["abcd","abce","bcdc","acde"]
print(equalization(n,m,s,t))
