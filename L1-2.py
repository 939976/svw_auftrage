#coding='utf-8'

import pandas as pd
import numpy as np

#输入数据
data= {'语文':[68,95,98,90,80],'数学':[65,76,86,88,90,],'英语':[30,98,88,77,90]}
index=["张飞","关羽","刘备","典韦","许褚",]
df = pd.DataFrame(data)
df.index=index #重新命名字索引

print("平均值是",'\n',df.mean())
print("最小值是",'\n',df.min())
print("最大值是",'\n',df.max())
print("无偏标准差是",'\n',df.std())
print("无偏方差是",'\n',df.var())

df['总成绩']=df.apply(lambda x: x.sum(),axis=1) #计算每行总成绩
print(df.sort_values(by='总成绩', ascending=False))

