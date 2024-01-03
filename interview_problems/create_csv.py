import pandas as pd
import csv
dict_data = {'Customer Id':[1,2,3,4,5],
             'Gender':["Male","Female","Male","Female","Male"],
             'Age':[25,24,23,27,28],
             'Income':[30000,40000,50000,60000,70000]
}
data = pd.DataFrame(dict_data) #creating a daraframe
data.to_csv('Customer.csv')
print(data)
