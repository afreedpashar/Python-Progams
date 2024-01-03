#print range of square of numbers in a given range

def square(x):
    return x*x

x = [square(x) for x in range(1,11)]
print(x)