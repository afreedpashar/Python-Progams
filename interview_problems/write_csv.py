import pandas as pd
import csv
dict_data={"a":[1,2,3,4,5],"b":[5,3,4,5,6],"c":[9,8,7,6,5]}
d = pd.DataFrame(dict_data)
d.to_csv("NewCsv.csv",index=False,header=["val1","val2","val3"])
print(d)

