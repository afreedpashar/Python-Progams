def isPallindrome(x):
    x = str(x)
    left = 0
    right = len(x)-1
    while left<right:
        if x[left]!=x[right]:
            return False
        left+=1
        right-=1
    return True
print(isPallindrome(1221))
print(isPallindrome('madam'))