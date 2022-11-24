import pandas as pd
import re

pd.set_option('display.max_rows', None)
data = pd.read_csv(r'D:\AiCore\week4\facebook-marketplaces-recommendation-ranking-system\clean_data\Products.csv')
df = pd.DataFrame(data)

def cleaning(clean):
    df[clean] = df[clean].str.replace('£','')
    df[clean] = df[clean].str.replace(',','')

cleaning('price')



print(df['price'])