import pandas as pd
import json

with open('declaraciones.json','r') as f:
    data = json.loads(f.read())

df_nested_list = pd.json_normalize(data)
df_nested_list.info()
print(df_nested_list.head())
df_nested_list.to_csv('data_declara2.csv', encoding='utf-8')
