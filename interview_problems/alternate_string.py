def mergeString(w1,w2):
    output =""
    i=j=0
    while len(w1)>i or len(w2)>j:
        if len(w1)>i:
            output+=w1[i]
            i+=1
        if len(w2)>j:
            output+=w2[j]
            j+=1
    return output

w1 = input("enter the words: ")
w2 = input("enter the words: ")
print(mergeString(w1,w2))