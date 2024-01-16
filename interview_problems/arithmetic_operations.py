import pandas as pd
var = pd.DataFrame({'A':[1,2,3,4],'B':[12,34,45,6]})
var["C"] = var["A"]+var["B"]
print(var)

#to check the values in between present or not or value is present or not
var = pd.DataFrame({"A":[10,20,30,40],"B":[11,25,30,45]})
var["value"] = var["A"]==30
var["value_1"] = var["B"] > 40
print(var)