import pandas as pd
import numpy as np
from scipy import stats
import os

df = pd.read_csv('scores.csv')
print(df.shape)
print(df)

fm = df.loc[df['gender'] == 'female', 'math score'].values
print(type(fm))
print(fm)

mm = df.loc[df['gender'] == 'male', 'math score'].values
print(type(mm))
print(mm)

print(mm.size,' , ', fm.size)


