import pandas as pd
csv_1 = pd.read_csv('C:\\pythonprograms\\pandas\\NewCsv.csv')
# print(csv_1.index)
print(csv_1.columns)
#describe function is used to get the values of min max 75% etc
# print(csv_1.describe)
print(csv_1[2:])

# csv_1.sort_index(axis=0,ascending=False) to get the values in descending order
# to change the vaues we use loc function
csv_1.loc[0,'val1']=1000
print(csv_1)