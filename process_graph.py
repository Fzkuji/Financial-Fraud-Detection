import pandas as pd

# # 节点处理
# data = pd.read_csv("datasets/SyntheticFinancialDatasets/syn_data.csv")
# # print(len(data))
# nameOrig = data['nameOrig'].drop_duplicates(keep='first', inplace=False).to_frame().rename(columns={'nameOrig': 'name'})
# # print(len(nameOrig))
# nameDest = data['nameDest'].drop_duplicates(keep='first', inplace=False).to_frame().rename(columns={'nameDest': 'name'})
# # print(len(nameDest))
# # print(nameDest)
# name = pd.merge(nameOrig, nameDest, how='outer', on='name').rename(columns={'name': 'userId:ID'})
# # print(len(name))
# name.to_csv("datasets/SyntheticFinancialDatasets/user.csv", index=0)


# # 关系处理
# data = pd.read_csv("datasets/SyntheticFinancialDatasets/syn_data.csv")
# data = data.rename(columns={'nameOrig': 'nameOrig:START_ID', 'nameDest': 'nameDest:END_ID', 'type': 'type:TYPE'})
# # print(len(name))
# data.to_csv("datasets/SyntheticFinancialDatasets/transfer.csv", index=0)


# # 另一种关系处理
# data = pd.read_csv("datasets/SyntheticFinancialDatasets/syn_data.csv")
# data = data.rename(columns={'nameOrig': 'nameOrig:START_ID', 'nameDest': 'nameDest:END_ID', 'isFraud': 'isFraud:TYPE'})
# # print(len(name))
# data.to_csv("datasets/SyntheticFinancialDatasets/transfer.csv", index=0)


# # 数据分析
# # 按照转账金额排序
# df = pd.read_csv('datasets/SyntheticFinancialDatasets/syn_data.csv')
# # 按照列值排序
# data = df.sort_values(by="amount", ascending=False)
# # 把新的数据写入文件
# data.to_csv('datasets/SyntheticFinancialDatasets/descending.csv', mode='w')

# 删除缺失数据

df = pd.read_csv('datasets/SyntheticFinancialDatasets/syn_data.csv')
# 按照列值排序
data = df.drop(df[((df.oldbalanceOrg - df.newbalanceOrig) != df.amount) | ((df.newbalanceDest - df.oldbalanceDest) != df.amount)].index)
# 把新的数据写入文件
data.to_csv('datasets/SyntheticFinancialDatasets/dropNone.csv', mode='w',  index=False)

