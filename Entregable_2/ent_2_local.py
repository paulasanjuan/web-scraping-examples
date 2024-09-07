import sys
import os

import datetime
import pandas as pd
import requests
import json
import eurostat


# 1. INE DATA
def get_inedata(url_ine):
    r = requests.get(url_ine)
    data = r.json()
    if data and 'Data' in data[0] and isinstance(data[0]['Data'], list):
        values_total = [item['Valor'] for item in data[0]['Data']]
        year = [item['Anyo'] for item in data[0]['Data']]
        df = pd.DataFrame({'Spanish total value': values_total, 'Year': year})
        return df
    else:
        print("Error: Unexpected JSON structure or missing data")
        
def ine_df(df):
    # DataFrame 1
    df = df.sort_values(by='Year')
    df = df.reset_index(drop=True)
    df1 = df.groupby('Year').sum().reset_index()
    df1.set_index('Year', inplace=True)
    return df1

# 2. Eurostat DATA
def ue_data(eurostat_code):
    data_list = eurostat.get_data(eurostat_code)
    # DataFrame 2
    df2 = pd.DataFrame(data_list)
    df2.columns = df2.iloc[0]
    df2.drop(df2.index[0], axis=0, inplace=True)
    column_map = {'geo\\TIME_PERIOD': 'geo'}
    df2 = df2.rename(columns=column_map)
    df2.drop('freq', axis=1, inplace=True)
    df2.drop('unit', axis=1, inplace=True)
    df2.query("age == 'TOTAL'")
    df2.drop('age', axis=1, inplace=True)
    df2 = df2[df2['ord_brth'] == 'TOTAL']
    df2.drop('ord_brth', axis=1, inplace=True)
    grouped_df2 = df2.groupby('geo').sum().reset_index()
    df2_final = grouped_df2.T
    df2_final.columns = df2_final.iloc[0]
    df2_final = df2_final[1:]
    df2_final.index.name = 'Year'
    df2_final.index = df2_final.index.astype('int64')
    return df2_final

# Get the data 
current_directory = os.getcwd()
file_name = 'datos_entregable_2'
time_stamp = datetime.datetime.now().strftime('%Y%m%d_h%Hm%M')
file_name = file_name + time_stamp + '.csv'
file_path = os.path.join(current_directory, file_name)

url_ine = 'https://servicios.ine.es/wstempus/jsCache/es/DATOS_TABLA/46682?tip=AM&'
data_ine = get_inedata(url_ine)
df_ine = ine_df(data_ine)

eurostat_code = 'demo_fabortord'
df_ue = ue_data(eurostat_code)

# 3. Merge DataFrames
df_merged = df_ine.merge(df_ue, on='Year')
columns_without_zeros = df_merged.columns[(df_merged != 0).all(axis=0)]
df_reduced = df_merged[columns_without_zeros]

# 4. pred_place_holder
df_reduced['pred_place_holder'] =1
df_reduced = df_reduced.reset_index()

# 5.1. Create a csv
df_reduced.to_csv(file_path, sep=',', encoding='utf-8')

# 5. To PowerBI
df_final = df_reduced.apply(pd.to_numeric, errors='coerce').fillna(0).astype('int64')
dict_final = df_final.to_dict(orient='records')
powerbi_url = 'https://api.powerbi.com/beta/ced2c552-7d1f-4731-aa3a-2f0ec9629e26/datasets/030832a3-3abf-479a-8bdc-b8b52682d16d/rows?experience=power-bi&key=%2Ft15aR5fRC1L9CQ7R1QBHhR3trk2Y%2B1xSVU8aXgD4hW7cQrQVE377PVcAOJuaaiQwvheyd0rsVrfssbR0VN0Pg%3D%3D'
headers = {'Content-Type': 'application/json'}
response = requests.request(
    method="POST",
    url=powerbi_url,
    headers=headers,
    data=json.dumps(dict_final)
)
print(response)
