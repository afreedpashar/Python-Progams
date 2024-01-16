import pandas as pd 
csv_1=pd.read_csv('C:\\pythonprograms\\interview_problems\\NewCsv.csv',nrows=2)
# print(csv_1)

#to get colums
csv_1=pd.read_csv('C:\\pythonprograms\\interview_problems\\NewCsv.csv',usecols=[0,1,2])
# print(csv_1)

#to skip particual row we use skiprow
csv_1=pd.read_csv('C:\\pythonprograms\\interview_problems\\NewCsv.csv',skiprows=[0,1])
# print(csv_1)

#name parameter
csv_1=pd.read_csv('C:\\pythonprograms\\interview_problems\\NewCsv.csv',dtype={'val1':'float'})
print(csv_1)


