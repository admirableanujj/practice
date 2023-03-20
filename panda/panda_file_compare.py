import os
import pandas as pd
import numpy as np
import configparser

config = configparser.RawConfigParser()

config_FILE_path = 'panda_file_compare.cfg'
config.read(config_FILE_path)

details_dict = dict(config.items('File_PATH'))

print(details_dict)
print("PATH", os.getcwd())
path  = os.getcwd()
path_to_sample_data = '/sample_data/'   
file1  = 'sample_data_1.xlsx'
file2 = 'sample_data_2.xlsx'

df1 = pd.read_excel(path+path_to_sample_data+file1, sheet_name=['Sheet1'])
print(df1['Sheet1'])
df2 = pd.read_excel(path+path_to_sample_data+file2, sheet_name=['Sheet1'])
print(df2['Sheet1'])

A = df1['Sheet1'].to_numpy()
X = df2['Sheet1'].to_numpy()

print(A)
print(X)
print(np.matmul(A,X))

