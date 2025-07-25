import pandas as pd
import  numpy as np

df = pd.DataFrame(np.arange(0,15).reshape((3,5)),index=['R1','R2','R3'],
                  columns=['Col1','Col2','Col3','Col4','Col5'])
print(df)
print('------------------------------')
print(df.iloc[:,:])
print('------------------------------')
print(df.iloc[:,1:])
print('------------------------------')
print(df.iloc[0:3,0:3])
print('---------------------')
print(df.iloc[0:3,0:4].values)
print(df.iloc[0:3,0:4].values.shape)
print('------------------------------')
print(df.isnull().sum())
print('----------------------------')
print(df['Col2'].value_counts())
print(df['Col2'].unique())
print('-----------------------------')
print(df[['Col1','Col2','Col3']])