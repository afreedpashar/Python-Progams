import pandas as pd
# var = pd.DataFrame({"A":[1,2,3,4,54],"B":[4,5,6,7,8]})
# var.insert(2,"C",[11,12,13,14,15]) #here 2 is index in column C is column name and those are values
# print(var)


#DELETE data in pandas
var1 = pd.DataFrame({"A":[1,2,3,4,54],"B":[4,5,6,7,8]})
var1.insert(2,"C",[2,3,4,5,6])
del var1["A"]
print(var1)