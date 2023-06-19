import os
from data_download import download_data, save_data

import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

ticker_symbol = "AAPL"
start_date = '20150-01-01'
end_date = '2023-06-15'
file_name = "AAPL.csv"
    
# 이미 데이터를 가져온 경우엔 실행하지 않음
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
    

plot_candlestick(df)