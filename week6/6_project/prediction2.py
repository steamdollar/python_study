import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
import pandas as pd
import datetime
import os
import sys
import math
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from build_model import build_model
from data_download import download_data, save_data
from plot_graph import plot_graph
from datetime import datetime, timedelta
from test_data import test_data

# ticker, 기간 지정
ticker_symbol = "AAPL"
start_date = '2010-01-01'
end_date = '2023-06-21'
file_name = "AAPL.csv"

# 이미 데이터가 있는 경우 데이터 다운로드를 실행하지 않음
if not os.path.exists(file_name):
    df = download_data(ticker_symbol, start_date, end_date)
    save_data(df, file_name)

df = pd.read_csv('AAPL.csv', index_col=0, parse_dates=True)

# 필요 column 선별
dataset = df.filter(['Open', "High", 'Low', 'Close']).values

# data period specify
training_data_len = math.ceil(len(dataset) * 0.8)

# normalize
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)

#
# training
train_data = scaled_data[0:training_data_len, :]
x_train, y_train = [], []

for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, :])
    # predicting the closing price
    y_train.append(train_data[i, :])
    
x_train, y_train = np.array(x_train), np.array(y_train)

model_path= 'saved_model2.h5'
model = build_model(model_path, x_train, y_train)

# test
rmse = test_data(model, dataset)

# # Plot the data
# train = df[:training_data_len]
# valid = df[training_data_len:].copy()
# valid['Predictions'] = predictions
# plot_graph(train['Close'], 'Model', 'Date', 'Close Price USD ($)', "pred2.png", ['Train', 'Val', 'Predictions'])

# practical prediction
future_days = 180  # for predicting stock prices for the next 180 days

# Take the last 60 days of data and transform it to the correct shape
last_60_days = scaled_data[-60:]

# .reshape(batch_size, time_steps, # of input_features)
# 인수들이 input 삼중배열의 형태를 결정
new_input = last_60_days.reshape(1, 60, 4)

future_predictions = []

# Predict future stock prices day by day
for i in range(future_days):
    # predict method는 각 시퀀스의 예측값을 리턴
    prediction = model.predict(new_input)
    
    future_predictions.append(prediction[0])
    
    new_prediction = np.zeros((1,1,4))
    new_prediction[0, 0, 3] = prediction[0, 0]
     
    new_input = np.append(new_input[:, 1:, :], new_prediction, axis=1)

# Inverse scaling the predictions
future_predictions = np.c_[np.zeros((len(future_predictions), 3)), future_predictions]
future_predictions = scaler.inverse_transform(future_predictions)[:, 3]

# Generating future dates

last_date = datetime.strptime(str(df.index[-1]), '%Y-%m-%d')
future_days = (datetime.datetime.strptime("2023-12-31", "%Y-%m-%d") - datetime.datetime.strptime("2023-06-21", "%Y-%m-%d")).days

# Plot the predictions

plot_graph(pd.concat([df['Close'], pd.Series(future_predictions, index=future_dates)]), 'AAPL Stock Price Prediction',
           'Date', 'Close Price USD ($)', 'pred3.png', ['Historical Data', 'Future Predictions'])