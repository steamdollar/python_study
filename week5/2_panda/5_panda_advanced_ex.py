#
# 1. handling missing data
# msiing value를 처리하는 다양한 method가 있다.
# fillna 함수는 n/a 값을 여러 방식으로 채워준다.

import pandas as pd
import numpy as np

# create a sampole datafrmae w/ NaN values
df = pd.DataFrame([[np.nan, 2, np.nan, 0],
[3, 4, np.nan, 1],
[np.nan, np.nan, np.nan, 5],
[np.nan, 3, np.nan, 4]],
columns=list("ABCD"))

print("Original DataFrame")
print(df)

print()
print("\nFill NA w/ a static value")
print(df.fillna(0))


print()
print("\nFill NA w/ the mean of the column")
print(df.fillna(df.mean()))

print()

#
# 2. Merging and joining DataSets
# 두 개의 샘플 데이터 프레임을 merge, join

df1 = pd.DataFrame({'A' : ['A0', 'A1', 'A2'],
'B' : ['B0', 'B1', 'B2']},
index=['K0', 'K1', 'K2'])

df2 = pd.DataFrame({
    'C' : ['C0', 'C2', 'C3'],
    'D' : ['D0', 'D2', 'D3']
}, index = ['K0', 'K2', 'K3'])

print('\nOriginal df1')
print(df1)


print('\nOriginal df2')
print(df2)

# index에 맞춰서 두 데이터 셋을 join
print('\nAfter Joining df1 and df2')
print(df1.join(df2))

print()

#
# 3. GroupBy Functionality

df3 = pd.DataFrame({
    'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C' : [1, 2, 3, 4, 5, 6, 7, 8],
    'D' : [9,10,11,12,13,14,15,16]
})


print("original data")
print(df3)

# A group을 기준으로 데이터를 묶음 
# bar 에 있는 행들을 전부 더함

print("\nGroupBy w/ single column A, aggreagation sum")
print(df3.groupby('A').sum())

# 'A', 'B' column 기준으로 데이터를 묶음
# 
print("\nGroupBy w/ multiple columns A & B, aggreagation mean")
print(df3.groupby(['A', 'B']).mean())