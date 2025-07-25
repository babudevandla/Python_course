import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(0,15).reshape((3,5)),index=['R1','R2','R3'],columns=['Col1','Col2','Col3','Col4','Col5'])
print(df)
print('------------------------------')
print(df.loc['R1'])
print(type(df.loc['R1']))