#
# 1. Handling missing Data
# 누락된 데이터들 혹은 제겋라 데이터를 어떻게 처리하는지
# 보통은 np.nan value를 사용해 data를 표현한다. 디폴트로 이는 계산에 포함되지 않음.

# NaN 값이 있는 행을 제거
df.dropna()

# NaN 값을 특정 값으로 채우기
df.fillna(value=5)

# 값들을 true/false로 변환 > NaN값은 true, vice versa
pd.isna(df)

#
# 2. Merging and Joining Datasets
# 다양한 로직을 이용해 Serires와 Dataframe을 합칠 수 있다.

df1.append(df2)
pd.concat([df1, df2])
pd.merge(df1, df2, on='common_column')
df1.join(df2)

#
# 3. GroupBy Functionality
# GroupBy method는 데이터 row를 그룹짓고, 모든 그룹에 적용되는 aggregate 함수를 호출

df.groupby('A').sum()
df.groupby(['A','B']).mean()

