#Python | Sort Python Dictionaries by Key or Value

# Input:
# {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

# Output: 
# {'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}

myDict =  {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
myKeys = list(myDict.keys())
myKeys.sort()
sortedDict = {i:myDict[i] for i in myKeys}
print(sortedDict)