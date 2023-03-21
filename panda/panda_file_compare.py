import os
import pandas as pd
import numpy as np
import configparser


config = configparser.ConfigParser()
config_FILE_path = 'C:/Users/anujj/OneDrive - University of Cincinnati/Projects/ProjectEuler/panda/panda_file_compare.cfg'
config.read(config_FILE_path)
    
details_dict = config.sections()
sample_file_name = dict(config.items('FILE'))
path_to_sample_file = dict(config.items('SAMPLE_DATA'))

# print("PATH", os.getcwd())
# path  = os.getcwd()
path_to_sample_data = path_to_sample_file['path']   
file1  = sample_file_name['name1']
file2 = sample_file_name['name2']

df1 = pd.read_excel(path_to_sample_data+file1, sheet_name=['Sheet1'])
print(df1['Sheet1'])
df2 = pd.read_excel(path_to_sample_data+file2, sheet_name=['Sheet1'])
print(df2['Sheet1'])

A = df1['Sheet1'].to_numpy()
X = df2['Sheet1'].to_numpy()

print(A)
print(X)
print(np.matmul(A,X))

