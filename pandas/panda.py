# how to create dataframe 
import pandas as pd 
dict_data = {'name':["Afreed","Nizam","Sheru","Irfan","Nawaz"],"age":[24,28,23,31,25],"work":["Software Engineer","Accountant","Accountant","Showroom","data analyst"]}
result = pd.DataFrame(dict_data,columns=['name','work'],index=[1,2,3,4,5])
print(result["name"][4]) #here we are getting particular value by passing column and index value