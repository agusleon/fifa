import gc
import sys
import numpy as np
import requests
import pandas as pd
from pandas.io.json import json_normalize
from datetime import datetime

# SeasonID corresponds to FIFA Worldcup 2014 in Brazil
url = "https://api.fifa.com/api/v1/calendar/matches?idSeason=251164&count=500&language=en"
# stages
# 	/api/v1/stages

def request_url(url):
    r = requests.get(url)
    if r.status_code == 200 :
        print("cool.")
    else:
        print("not cool.")
        gc.collect()
        sys.exit()
    return r

def transform_to_dataframe(r):
    fifa_json = r.json()['Results']
    df = pd.json_normalize(fifa_json, max_level=1)
    return df

def display_info(df):
    print("The data is like...\n",df.head(10))
    print(df.info())

def delete_nulls(df):
    df_not_null = df.dropna(axis=1, how='all')
    return df_not_null

def to_csv(df):
    data_csv = df.to_csv("fifa_worldcup_2014_data.csv")
    return data_csv

query = request_url(url)
raw_data = transform_to_dataframe(query)
#display_info(data)
data = delete_nulls(raw_data)
file = to_csv(data)
