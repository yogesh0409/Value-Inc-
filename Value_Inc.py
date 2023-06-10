import pandas as pd
import numpy as np
import seaborn as sns

data=pd.read_csv('transaction.csv')
data=pd.read_csv('transaction.csv',sep=';')




#summary
data.info()



#Checking cost values for per item
data['CostPerTransaction']=data['CostPerItem']*data['NumberOfItemsPurchased']

#Checking sell values for per item
data['SalesPerTransaction']=data['SellingPricePerItem']*data['NumberOfItemsPurchased']

#Checking profit values for per item
data['profitPerTransaction']=data['SalesPerTransaction']-data['CostPerTransaction']

#Checking profit margin values for per item
data['ProfitMargin']=round((data['SalesPerTransaction']-data['CostPerTransaction'])/data['CostPerTransaction'],2)

#changing the data type for days and year
data['Day']=data['Day'].astype(str)
data['Year']=data['Year'].astype(str)

data.info()
#Combining the date in the data
data['Date']=data['Day']+'-'+data['Month']+'-'+data['Year']

#spilting the field 

split_col=data['ClientKeywords'].str.split(',',expand=True)
split_col
#Spliting the data in three columns
data['ClientAge']=split_col[0]
data['ClientType']=split_col[1]
data['ContractYear']=split_col[2]


#replacing the unnecessary things

data['ClientAge']=data['ClientAge'].str.replace('[','')
data['ClientAge']=data['ClientAge'].str.replace("'",'')
data['ContractYear']=data['ContractYear'].str.replace(']','')
data['ContractYear']=data['ContractYear'].str.replace("'",'')
data['ClientType']=data['ClientType'].str.replace("'",'')

#using lower function to change itemdescription
data['ItemDescription']=data['ItemDescription'].str.lower()



#joining the two data sets

data1=pd.read_csv('value_inc_seasons.csv',sep=';')

data=pd.merge(data,data1,on='Month')

 #dropping the unnecessary field
data=data.drop(['ClientKeywords','Year','Month','Day'],axis=1)

#exporting the datset into csv
data.to_csv('valueinc_cleaned.csv',index = False)
























