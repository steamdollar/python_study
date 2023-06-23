import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model
import pandas as pd
import datetime
import os
import math
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

model = load_model("saved_model.h5")

file_name="AAPL.csv"
df = pd.read_csv(file_name, index_col=0, parse_dates=True)

data = df.filter(['Open', "High", 'Low', 'Close'])
dataset = data.values
training_data_len = math.ceil(len(dataset) * 0.8)
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(dataset)

# create training dataset
train_data = scaled_data[0:training_data_len, :]
x_train, y_train = [], []
for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, :])
    # predicting the closing price
    y_train.append(train_data[i, 3])
    
x_train, y_train = np.array(x_train), np.array(y_train)

model_path= 'saved_model2.h5'

if not os.path.exists(model_path):
    model = Sequential()
    model.add(LSTM(128, return_sequences=True, input_shape= (x_train.shape[1], 4)))
    model.add(LSTM(64, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1)) 

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, batch_size=1, epochs=10)
    model.save(model_path)
else:
    model = load_model(model_path)

# ...assuming you have completed the model training code above...

# Create a new dataset for testing
test_data = scaled_data[training_data_len - 60:, :]
x_test, y_test = [], dataset[training_data_len:, 3]
for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i, :])

# Convert the data to a numpy array
x_test = np.array(x_test)

# Get the models predicted price values
predictions = model.predict(x_test)

# We have scaled the predictions between 0 and 1, we now need to inverse the scaling
predictions = np.c_[np.zeros((len(predictions), 3)), predictions]
predictions = scaler.inverse_transform(predictions)[:, 3]

# Calculate the RMSE to check accuracy of predictions
rmse = np.sqrt(np.mean(predictions - y_test) ** 2)

print("Root Mean Squared Error:", rmse)

# Plot the data
train = data[:training_data_len]
valid = data[training_data_len:].copy()
valid['Predictions'] = predictions

plt.figure(figsize=(16, 8))
plt.title('Model')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.savefig("pred2.png")


#
future_days = 180  # for predicting stock prices for the next 180 days

# Take the last 60 days of data and transform it to the correct shape
last_60_days = scaled_data[-60:]
new_input = np.array([last_60_days])

future_predictions = []

# Predict future stock prices day by day
for i in range(future_days):
    prediction = model.predict(new_input)
    future_predictions.append(prediction[0, 0])
    
    new_prediction = prediction[:, 0:1]
    new_input = np.append(new_input[:, 1:, :], new_prediction.reshape(1, 1, 1), axis=1)

# Inverse scaling the predictions
future_predictions = np.c_[np.zeros((len(future_predictions), 3)), future_predictions]
future_predictions = scaler.inverse_transform(future_predictions)[:, 3]

# Generating future dates
from datetime import datetime, timedelta
last_date = datetime.strptime(df.index[-1], '%Y-%m-%d')
future_dates = [last_date + timedelta(days=x) for x in range(1, future_days + 1)]

# Plot the predictions
plt.figure(figsize=(16, 8))
plt.title('AAPL Stock Price Prediction')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.plot(df['Close'], label='Historical Data')
plt.plot(future_dates, future_predictions, label='Future Predictions')
plt.legend(loc='lower right')
plt.show()
