import pandas as pd
import numpy as np
import os

def change_type(df, type):
  for col in df.columns: 
    try:
      df[col] = df[col].astype(type)
      if type == 'int' or type == 'float':
        #appy transform numbers
        df = transform_numbers(df, col)
    except:
      pass
  return df

def clean_data(df, type='float'):
  df = change_type(df, 'str')
  df = change_type(df, type)
  df = df.drop_duplicates()
  df = df.dropna()
  df = df.dropna(axis=1, how='all')
  df = df.reset_index(drop=True)

  return df

def transform_numbers(df, column):
    df[column] = df[column].str.replace('.', '')
    df[column] = df[column].str.replace(',', '.')
    df[column] = df[column].str.replace(' ', '')
    df[column] = df[column].str.replace('-', '')
    df[column] = df[column].str.replace('R\$', '')
    df[column] = df[column].str.replace('%', '')
    df[column] = df[column].str.replace('R', '')
    df[column] = df[column].str.replace('$', '')
    df[column] = df[column].str.replace('(', '')
    df[column] = df[column].str.replace(')', '')
    df[column] = df[column].str.replace(';', '')
    df[column] = df[column].str.replace('=', '')
    df[column] = df[column].str.replace('>', '')
    df[column] = df[column].str.replace('<', '')
    df[column] = df[column].str.replace('?', '')
    df[column] = df[column].str.replace('!', '')
    df[column] = df[column].str.replace('@', '')
    df[column] = df[column].str.replace('#', '')
    df[column] = df[column].str.replace('&', '')
    df[column] = df[column].str.replace('*', '')
    df[column] = df[column].str.replace('/', '')
    df[column] = df[column].str.replace('|', '')
    df[column] = df[column].str.replace('\\', '')
    df[column] = df[column].str.replace('\'', '')
    df[column] = df[column].str.replace('\"', '')
    df[column] = df[column].str.replace('[', '')
    df[column] = df[column].str.replace(']', '')
    df[column] = df[column].str.replace('{', '')
    df[column] = df[column].str.replace('}', '')
    df[column] = df[column].str.replace('~', '')
    df[column] = df[column].str.replace('^', '')
    df[column] = df[column].str.replace('`', '')
    df[column] = df[column].str.replace('_', '')
    df[column] = df[column].str.replace('+', '')
    df[column] = df[column].str.replace(':', '')

    return df