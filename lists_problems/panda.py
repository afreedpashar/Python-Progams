import pandas as pd

# car = [1,3,5,7]
# myvar = pd.Series(car,index=['a','b','c','d'])
# print(myvar['c'])

# data = {
#     "cars":["bmw","kia","ferrari","audi"],
#     "bikes":["suzuki","Honda","hero","bajaj"]
# }
# myvar = pd.DataFrame(data)
# print(myvar.loc[[0,1]])


data ={
    'months' : ["jan","feb","march"],
    'weeks':["sun","mon","tues"],
}
myvar = pd.DataFrame(data,index=['first','second','third'])
print(myvar.loc['first'])