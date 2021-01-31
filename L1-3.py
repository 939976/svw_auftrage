#coding='utf-8'

import numpy as np
import pandas as pd

#数据加载
df = pd.read_csv('car_complain.csv')
#将问题分类
df= df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))
#将数据整理
df['brand'] = df['brand'].apply(lambda x: x.replace('一汽-大众','一汽大众'))

#品牌投诉总数
result=df.groupby('brand')['id'].agg(['count'])
#result.to_csv('./result3.csv')

#车型投诉总数
result2=df.groupby('car_model')['id'].agg(['count'])
result2= result2.sort_values(by='count',ascending=False)
result2.reset_index(inplace=True)#正常列
#result2.to_csv('./result3.csv')

#平均投诉总数
result3_1=df.groupby('brand')['id'].agg(['count'])
result3_1.reset_index(inplace=True) #正常列
result3_3=df.groupby(['brand'])['car_model'].nunique()
a = {'brand':result3_3.index,'num':result3_3.values}#转换为DataFrame
result3_2=pd.DataFrame(a)
result3=pd.merge(result3_1,result3_2,how='outer')#合并结果
result3['result']=result3.apply(lambda x: x['count']/x['num'],axis=1)#计算平均值
result3=result3.sort_values(by='result',ascending=False)
result3=result3.reset_index(drop=True)
#result3.to_csv('./result3.csv')





