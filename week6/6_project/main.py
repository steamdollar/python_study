import os
from data_download import download_data, save_data
import math
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# ticker, 기간 지정
ticker_symbol = "AAPL"
start_date = '2010-01-01'
end_date = '2023-06-15'
file_name = "AAPL.csv"
    
# 이미 데이터가 있는 경우 데이터 다운로드를 실행하지 않음
if not os.path.exists(file_name):
    df = download_data(ticker_symbol, start_date, end_date)
    save_data(df, file_name)

df = pd.read_csv('AAPL.csv', index_col=0, parse_dates=True)

# Preprocessing

# 캔들 차트 드로잉 함수
def plot_candlestick(df):
    fig = go.Figure(data=[go.Candlestick(x=df.index,
    open=df['Open'],
    high=df['High'],
    low=df["Low"],
    close=df["Close"])])
    
    fig.update_layout(title="AAPL CnadleStick Chart",
    xaxis_title="Date",
    yaxis_title="Price (USD $)",
    xaxis_rangeslider_visible=False)
    
    fig.show()
    
# 주석을 풀면 차트를 브라우저에 그려준다.
# 하짐나 가격 예측에 굳이 차트를 그릴 필요는 없으므로 여기선 이렇게 그릴 수 있다는 정도만 알면 될 듯.
# plot_candlestick(df)

from sklearn.preprocessing import MinMaxScaler
import numpy as np

# data split

dataset = df.filter(['Close']).values

training_data_len = math.ceil(len(dataset)* 0.8)

# normalize
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)

# scaled training data set
# dataset의 slice > matrix이므로 범위를 특정하기 위해서는 row, column 둘에 대한 매개 변수가 모두 필요함
# 첫 번째가 row > 0 ~ training_data_len 까지 = 모든 행
# 두 번째가 column > 특정된 row에 대한 모든 column
train_data = scaled_data[0:int(training_data_len), :]

# split the data into x_train and y_train
x_train = []
y_train = []

for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])
    
# Convert the x_train and y_train to numpy arrays 
x_train, y_train = np.array(x_train), np.array(y_train)