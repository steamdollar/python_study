import os
import yfinance as yf

def download_data(ticker, start_date, end_date):
    ticker_data = yf.Ticker(ticker)
    df = ticker_data.history(period='id', start=start_date, end=end_date)
    
    return df
    
def save_data(df, file_name):
    df.to_csv(file_name)

# 필수적인 코드는 아니고, 테스트용
# data_dwonload.py 직접 이 파일을 직접 파이썬으로 실행할 경우에만 이게 실행된다.
if __name__ == "__main__":
    ticker = "AAPL"
    start_date = "2010-01-01"
    end_date = "2023-06-15"
    file_name = "AAPL.csv"
    
    if not os.path.exists(file_name):
        df = download_data(ticker, start_date, end_date)
        save_data(df, file_name)