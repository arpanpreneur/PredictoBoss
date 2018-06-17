import Config.DataSource as ds
import numpy as np
import pandas as pd
from dateutil import parser

data_source = ds.DataSource()
db = data_source.getDB()

def correct_dates(data):
    data_mod = {}

    for item in list(data.keys()):
        temp = parser.parse(str(item))
        data_mod[temp] = data[item]

    return data_mod

def getDataSet_petrol(date):
    petrol_col = db['processed_data_petrol']
    data = petrol_col.find_one({"obtained_on":str(date)},{"_id":0,"obtained_on":0})

    df = pd.DataFrame(list(correct_dates(data).items()),columns=['date','price'])
    df['date'] = pd.to_datetime(df['date'])

    return df

def getDataSet_diesel(date):
    petrol_col = db['processed_data_diesel']
    data = petrol_col.find_one({"obtained_on":str(date)},{"_id":0,"obtained_on":0})

    df = pd.DataFrame(list(correct_dates(data).items()),columns=['date','price'])
    df['date'] = pd.to_datetime(df['date'])

    return df

#print(getDataSet_petrol("16-06-2018"))



