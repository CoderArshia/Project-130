import pandas as pd 
import csv 

df = pd.read_csv("total_stars.csv")
del df ["Luminosity"]

print(df.shape)
print(list(df))


df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1'],axis=1,inplace=True)

print(df)

df.to_csv("final_data.csv")