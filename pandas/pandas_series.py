import pandas as pd
sr = {"s":pd.Series([1,2,3,4]),"r":pd.Series([5,6,7,8])}
# print(sr)
#to merge the series into dataframe

var = pd.DataFrame(sr)
print(var)