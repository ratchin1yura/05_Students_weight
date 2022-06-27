# import numpy as np
import pandas as pd
from tabulate import tabulate

columns1 = range(1, 9)

data1 = pd.read_csv('NYSDOH_SWSCR_CountyData_2008_2010.csv', delimiter=',', usecols=columns1)

look_column = 'COUNTY_NAME'
look_text = 'Washington'

data1 = data1[data1[look_column].str.contains(look_text)]

print(f'Статистика по {look_text}:')
print(data1.columns.tolist())

print(tabulate(data1, headers=data1.columns.tolist()))
