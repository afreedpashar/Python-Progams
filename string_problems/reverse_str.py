def rev(s):
    output = ""
    i = len(s)-1
    while i>=0:
        output = output+s[i]
        i=i-1
    return output
s= "afreed"
print(rev(s))

"""here i have taken output is empty string , i = len(s)-1 because to get the last char of a string and then 
when i >=0 i will run a while loop and output =output+s[i] it will  keep on adding last word ans we need to decrement
the string by i=i-1"""