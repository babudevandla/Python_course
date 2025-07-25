import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'], columns=['Column1','Column2','Column3','Column4'])
print(df.head())
print(type(df))
print(df.shape)
print('----------------')

df.to_csv('Test1.csv')
