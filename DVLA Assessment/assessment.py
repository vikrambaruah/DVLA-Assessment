import pandas as pd
import random
import datetime
data = pd.read_csv("data.csv")
random_numbers = [str(random.randint(1000, 9999)) for _ in range(len(data))]
data['country_code'] = ''
total_countries={}
for i in range(len(data)):
    if str(data.loc[i, 'Country of Birth']) == 'England':
        data.loc[i, 'country_code'] = 'E'
    elif str(data.loc[i, 'Country of Birth']) == 'Scotland':
        data.loc[i, 'country_code'] = 'S'
    elif str(data.loc[i, 'Country of Birth']) == 'Wales':
        data.loc[i, 'country_code'] = 'W'
    elif str(data.loc[i, 'Country of Birth']) == 'Northern Ireland':
        data.loc[i, 'country_code'] = 'N'
    else:
        data.loc[i, 'country_code'] = 'O'

data['NIN'] = data['First names'].str[0] + data['Last name'].str[0]+pd.to_datetime(data['Date of Birth']).dt.strftime('%y')+random_numbers+data['country_code']
data2 = pd.DataFrame(data['country_code'].value_counts()).reset_index()
data2.columns = ['country_code', 'count']


#data.to_csv("NIN.csv")
with pd.ExcelWriter("NIN.xlsx") as writer:
    data.to_excel(writer, sheet_name="NIN", index=False)
    data2.to_excel(writer, sheet_name="Total", index=False)
#print(data)
