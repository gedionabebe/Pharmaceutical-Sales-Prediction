import numpy as np
import pandas as pd
import logging
from sklearn.preprocessing import LabelEncoder, StandardScaler

logging.basicConfig(filename='../log/log.log', filemode='a',encoding='utf-8', level=logging.DEBUG)

def datetime(df,column):
    df[column] = pd.to_datetime(df[column])
    return df[column]

def numeric(df,column):
    df[column]= pd.to_numeric(df[column])
    return df[column]

def fill_ffill(df,column):
    df[column] = df[column].fillna(method='ffill')
    return df[column]

def fill_bfill(df,column):
    df[column] = df[column].fillna(method='bfill')
    return df[column]

def fill_mean(df,column):
    df[column] = df[column].fillna(df[column].mean())
    return df[column]

def fill_mode(df,column):
    df[column] = df[column].fillna(df[column].mode())
    return df[column]

def label_encode(df,column):
    df[column] = LabelEncoder().fit_transform(df[column])
    return df[column]

def scale_data(df):
    df = StandardScaler().fit_transform(df)
    return df
