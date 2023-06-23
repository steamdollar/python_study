import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
import pandas as pd
import datetime

model = load_model("saved_model.h5")

file_name="AAPL.csv"
df = pd.read_csv(file_name, index_col=0, parse_dates=True)

# 직전 60일의 정보를 사용해 미래 주가를 예측
last_60_days = df['Close'][-60:].values

# 표준화
scaler = MinMaxScaler()
last_60_days_scaled = scaler.fit_transform(last_60_days.reshape(-1, 1))

future_predictions = []
future_days = (datetime.datetime.strptime("2023-12-31", "%Y-%m-%d") - datetime.datetime.strptime("2023-06-21", "%Y-%m-%d")).days

# 재귀적으로 미래 주가 예측
for i in range(future_days):
    prediction = model.predict(np.array([last_60_days_scaled]).reshape(1, 60, 1))
    
    future_predictions.append(scaler.inverse_transform(prediction)[0, 0])
    last_60_days_scaled = np.append(last_60_days_scaled[1:], prediction)
    last_60_days_scaled = last_60_days_scaled.reshape(-1, 1)
    
for i in range(future_days):
     print(f"Prediction for {datetime.datetime.strptime('2023-06-21', '%Y-%m-%d') + datetime.timedelta(days=i)}: ${future_predictions[i]}")
    

