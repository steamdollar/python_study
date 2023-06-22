import os
from data_download import download_data, save_data
import math
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

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

# pip install tensorflow, keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.models import load_model

model_path = 'saved_model.h5'

# Build the LSTM model

if not os.path.exists(model_path):
# build initialize neural network
    model = Sequential()

    # add 각 128, 64개의 뉴런을 가진 lstm layer를 추가
    # return_sequence를 true로 설정하면 output이 다음 lstm layer로 전달될 수 있다.
    model.add(LSTM(128, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(LSTM(64, return_sequences=False))

    # dense layer를 추가, 첫 번째는 25개 뉴런이, 두 번째는 1개 뉴런이 있다.
    model.add(Dense(25))
    model.add(Dense(1))

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # LSTM은 시계열 데이터이므로 데이터를 넣을때 3차원 데이터를 넣어줘야 함.
    # 1. # of samples : 데이터 셋에 포함된 데이터 포인트 수 혹은 시퀀스
    # 2. time steps : length of the sequence, 예를 들어 다음 날짜의 주가를 예측하기 위해 이전 60일간 데이터를
    # 사용한다면 60일 넣어주면 된다.
    # 3. feature : 각 time step을 represent하기 위해 사용되는 attribute의 수. 
    # 여기서는 stock price만을 사용하므로 1


    # 모델을 학습시키기 전에 x_train data의 형태를 바꿔 LSTM layer의 input으로 사용할 수 있도록 한다.
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    # model을 훈련
    # x_train : input data for training the model (reshaped stock price for the training data)

    # y_train : target data for training (stock prices that we want the model to learn to predict)

    # batch_size : gradient update를 샘플 몇개마다 할것인지를 지정하는 매개변수
    # 1로 설정했다면 모든 샘플마다 weight을 업데이트해준다.
    # batch 크기가 작을수록 regularization 효과가 크지만 속도가 느려진다.

    # epochs : 모든 input data (x, y 배열 전부)에 대한 반복 횟수.
    # 보통 모델은 여러 번의 epoch를 거쳐 학습이 진행된다.
    # epoch 기간 동안 모델은 예측 오류를 최소화하기 위해 각 weight를 조정한다.
    # 너무 횟수가 크면 overfit이 일어날 수 있고, vice versa

    model.fit(x_train, y_train, batch_size=1, epochs=5)
    model.save(model_path)
else:
    model = load_model(model_path)

# 학습된 모델을 사용해 test data에 대한 예측을 진행하고, 성능을 확인해보자.
test_data = scaled_data[training_data_len - 60: , :]

# create dataset 
x_test = []
y_test = df['Close'][training_data_len:].values

for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i, 0])

# convert, reshape data     
x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# 예측 price 값을 생성
predictions = model.predict(x_test)

# undo scaling
predictions = scaler.inverse_transform(predictions) 

# get RMSE (root mean square error)
rmse = np.sqrt(np.mean(((predictions - y_test) ** 2)))
print("==================")
print(f'RMSE: {rmse}')
print("==================")

# Plot/create data for the graph
train = df[:training_data_len]
valid = df[training_data_len:].copy()
valid["Predictions"] = predictions

# 시각화
plt.figure(figsize=(16, 8))
plt.title('Model')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.savefig("pred.png")