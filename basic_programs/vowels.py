def check(string):
    string = string.lower()
    vowels = set("aeiou")
    s = set({})

    for ch in string:
        if ch in vowels:
            s.add(ch)
        else:
            pass
    
    if len(s)==len(vowels):
        print( string, "accepted")
    else:
        print(string, "not accepted")

string =input("Enter a string: ") 
check(string)