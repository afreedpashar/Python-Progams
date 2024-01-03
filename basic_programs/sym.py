#symmetriccal and pallindrome

string1 = input("enter a string : ")
half = int(len(string1)/2)
first_str = string1[:half]
second_str = string1[half:]

if first_str == second_str:
    print(string1,"symmetrical")
else:
    print(string1,"non symmetrical")

if first_str == second_str[::-1]:
    print(string1,"pallindrome")
else:
    print(string1,"not a pallindrome")