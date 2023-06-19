# 0. intro
자동 매매 프로그램을 만들기 위해

timeforcasting system을 만들어보자.

시계열 예측에는 ARIMA, SARIMA,LSTM network, Facebook의 Prophet 등 다양한 테크닉이 있다.

목표는 과거 데이터 포인트를 기반으로 미래 데이터 포인트를 예측하는 모델을 만드는 것.

작업은 크게 5단계로 나눌 수 있다.

1. Data collection : 주식 가격의 역사적 데이터를 얻어야 하는데, 다양한 금융 관련 조직이 관련된 데이터나 api를 제공한다. 

2. Data Preprocessing : data를 다듬고, 필요하다면 보다 정교한 model을 위해 수정한다.

3. model building : 예측 모델을 선택하고 데이터를 학습시킨다.

4. Model evaluation : 다양한 경우에 대해 모델의 성능을 시험한다.

5. Forecasting : 실전 투입

당연히 주식은 다양한 요소에 의해 영향을 받고, 이는 과거 데이터에서는 확인할 수 없는 것일 수 있다.

적당히 좋은 모델을 만드는 것, 이를 통해 의사 결정에 도움이 되는 걸 목표로 하자.

# 1. data collection

난 미국 주식에 참여하고 싶다.

관련 데이터는 야후 파이낸스, 구글 파이낸스 등에서 얻을 수 있고, api를 제공해주는 것도 있음.

파이썬에서는 yfinance lib를 이용해 야후 파이낸스에서 데이터를 다운 받을 수 있다.

``` bash
    pip install yfinance
```

종목을 지정하고 데이터를 받아오면 된다.

# 2. preprocess

받아온 데이터를 가지고 preprocess를 진행한다.

캔들 차트를 보고 싶다면 plotly 라이브러리를 사용한다.

``` bash
    pip install plotly
```

2.1 Exploratory data analysis
2.2 preprocessing the data
2.3 creating and training the model
2.4 evaluating the model
2.5 forecasting future price

