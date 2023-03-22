import os
import pandas as pd
import numpy as np
import configparser
import string


def match_percent(x,y):
    return x+y


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

data1 = pd.read_excel(path_to_sample_data+file1, sheet_name=['Sheet1'])
df1_sheet1 = data1['Sheet1']
data2 = pd.read_excel(path_to_sample_data+file2, sheet_name=['Sheet1'])
df2_sheet1 = data2['Sheet1']
# df1 = pd.DataFrame.from_dict(data1, orient='index')
# df2 = pd.DataFrame.from_dict(data2, orient='index')

compare_df  = pd.DataFrame()
# compare_df['A']=pd.Series([10,20,30],index=['a','b','c'])
# compare_df["A"] = None
# compare_df["A"] = np.where(df1_sheet1['A']+df2_sheet1['X'] >=20, 'True', 'False')
r,c = df1_sheet1.shape
np.full((r,c),np.nan)
asciilower = list(string.ascii_lowercase)
compare_df=pd.DataFrame(data=np.full((r,c),np.nan),index=asciilower[:c])
compare_df["c"] = np.where(df1_sheet1['X']+df2_sheet1['A'] >=5, 10, 11)
print(df1_sheet1)
print(df2_sheet1)
print(compare_df)




# A = df1['Sheet1'].to_numpy()
# X = df2['Sheet1'].to_numpy()
# print(A)
# print(X)
# print(np.matmul(A,X))

