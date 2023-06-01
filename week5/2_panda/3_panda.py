#
# 1. What is panda?
# panda는 데이터 분석과 조작을 위한 라이브러리 (아마 외장인듯)
# pip install pandas
import numpy as np
import pandas as pd

# Series : 어떤 데이터 타입이든 넣을 수 있는 1차 labeled array
# 단, 모든 요소는 같은 타입이어야 함. 엑셀 시트의 칼럼과 동일하다.

# Dataframe : 다른 데이터 타입을 가질 수 있는 2차원
# index를 공유하는 Seires group

# 
# 2. creating dataframes and Series
# index를 공유하는 Series의 그룹이라고 생각하면 된다.
# 우선 Series를 생성.
# value의 list를 넣어 series를 생성해 pandas가 default integer index 생성

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# 데이터프레임은 잠재적으로 다른 유형의 열이 있는 2차원 레이블이 지정된 데이터 구조. 
# 스프레드시트나 SQL 테이블 또는 시리즈 객체의 사전처럼 생각할 수 있다.

dates = pd.date_range('20230101', periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

# ABCD는 column name, dates가 raw name
# 이건 csv와 동일함. 다음과 같은 함수를 사용할 수도 있다.
# df = pd.read_csv('mydata.csv')

print("=====================")

#
# 3. Basic Operations on Dataframes
# Dataframes에서 데이터를 조작, 요약하는 방법이 있다.

# Viewing data
# 디폴트로는 첫 5 rows 지정
print(df.head())
print("=====================")

# 마지막 3줄 지정
print(df.tail(3))
print("=====================")

#
# index, columns, 기저의 NumPy data를 확인
print(df.index)
print(df.columns)
print(df.to_numpy())

print()
print("======= describe() ======")
# data에 대한 오버 뷰 ( 통계적 특성 )
print(df.describe())

def printline(func):
    print()
    print("===== " + f"{func}" + " =====")
    
# data transposing (행, 렬 교환)
printline("transposing")
print(df.T)

# axis로 정렬 (오름차순 / 내림차순)
printline("sort by axis")
print(df.sort_index(axis=1, ascending=False))

# 값으로 정렬
printline("sort by value")
print(df.sort_values(by='B'))

# indexing and slicing으로 data 선택
printline("selection of data")
print(df['A'])
print(df[0:3])
print(df['20230102': '20230104'])

# selection by label
printline("label")
print(df.loc[dates[0]])
print(df.loc[:, ["A", "B"]])

# selection by position
printline("select-position")
print(df.iloc[3])

# boolean-indexing
# 조건을 만족하는 열을 선택
printline("boolean indexing")
print(df[df['A'] > 0 ])