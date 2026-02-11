import pandas as pd

df = pd.read_csv(r"C:\Users\91832\Downloads\orders.csv")

df.head(10)

#converting to null

df['Ship Mode'].unique()

#handle null values

df = pd.read_csv(r"C:\Users\91832\Downloads\orders.csv", na_values=['Not Available','unknown'])
df['Ship Mode'].unique()

#renamae column names make them into lower case and replace space with underscore
df.columns = df.columns.str.lower()
df.columns
df.columns =df.columns.str.replace(' ', '_')
df.columns

df.rename(columns={'Order Id' : 'order_id', 'City' : 'city'})

#adding new columns discount, sale_price and profit
#discount
df['list_price']*df['discount_percent']*.01
df['discount'] = df['list_price']*df['discount_percent']*.01
df
#sales_price

df['list_price'] - df['discount']
df['sales_price'] = df['list_price'] - df['discount']

df
#profit

df['profit'] = df['sales_price'] - df['cost_price']


#separate the profit and loss columns
import numpy as np

# create loss column
df['loss'] = np.where(df['profit'] < 0, abs(df['profit']), 0)

# keep only positive profit in profit column
df['profit'] = np.where(df['profit'] < 0, 0, df['profit'])

#converting the order_date from object data type to date
df.dtypes

df['order_date']= pd.to_datetime(df['order_date'], format='%Y-%m-%d')

#drop unwanted columns 
df.drop(columns=['discount_percent','list_price'], inplace =True)

df.to_csv(r"C:\Users\91832\Downloads\cleaned_orders.csv", index=False)


df
