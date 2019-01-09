import numpy as np
import pandas as pd

# 读取excel中某一列
data = pd.read_excel("XXXXX.xlsx",
                     # sheet_name = ' ',
                     header = None,
                     # index_col =[0],
                     usecols=[3])
array = data.values

# 转化为列表形式
list = []
for k in array:
    for j in k:
        list.append(j)

# 根据统计条件筛选要删除的元素，保存为列表，这里是删除元素个数为1的
delete = []
for i in set(list):
    if list.count(i) == 1:
        delete.append(i)

# 获得最后保留的元素列表
ret = []
for item in list:
    if item not in delete:
        ret.append(item)

# 读取原表格所有数据
dataframe = pd.read_excel("XXXXX.xlsx", header = None)

# 保存筛选出的元素所在行
result = dataframe[dataframe[3].isin(ret)]
print(result)
print(len(list),len(delete),len(ret))

# 将最终数据保存为新的文件
result.to_excel('XX.xlsx', index = False)