# data collection

import yfinance as yf

tickerSymbol = "AAPL"

tickerData = yf.Ticker(tickerSymbol)

df = tickerData.history(period='id', start='2010-1-1', end='2023-6-15')
df.to_csv('AAPL.csv')

# 2. preprocessing
import matplotlib.pyplot as plt
import pandas as pd

df.index = pd.to_datetime(df.index)

print(df.head())

plt.figure(figsize=(14,7))
plt.grid(True)
plt.xlabel('Data')
plt.ylabel('Closing Price ($)')

plt.plot(df['Close'])
plt.title('Apple Inc. closing Price')

plt.savefig('appl.png')

from sklearn.model_selection import train_test_split

# isolate the 'Close' function
close_price = df[['Close']]

train_data, test_data = train_test_split(close_price, train_size=0.8, shuffle=False)

print("Train data size:", len(train_data))
print("Test data size:", len(test_data))