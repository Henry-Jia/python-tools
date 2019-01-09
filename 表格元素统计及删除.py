import numpy as np
import pandas as pd


data = pd.read_excel("定边县.xlsx",
                     # sheet_name = '样本匹配',
                     header = None,
                     # index_col =[0],
                     usecols=[3])
array = data.values

list = []
for k in array:
    for j in k:
        list.append(j)

delete = []
for i in set(list):
    if list.count(i) == 1:
        delete.append(i)

ret = []
for item in list:
    if item not in delete:
        ret.append(item)


dataframe = pd.read_excel("定边县.xlsx", header = None)
result = dataframe[dataframe[3].isin(ret)]
print(result)
print(len(list),len(delete),len(ret))
result.to_excel('定边.xlsx', index = False)