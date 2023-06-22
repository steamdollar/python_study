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
//

LSTM을 이용해 실제 가격 예측을 진행해보자.

LSTM (long short term memory)는 Recurrent Neural Network, 순환 신경망 (RNN)의 일종이다. LSTM에는 피드백 연결이 있다. 이미지같은 단일 데이터 포인트에 더해 음서, 영상 등의 전체 데이터 시퀀스로 처리할 수 있다.

만약 다음 날의 주식 가격을 예측하고 싶다면 이전 날들의 주식 가격을 input으로 주면 된다.

lstm은 긴 시퀀스의 정보를 사용해 예측을 수행한다.

@ RNN (Recurrent Neurtal Networks)
텍스트, 유전자, 음성, 손글씨 등의 데이터 시퀀스의 패턴을 인식하도록 설계된 인공 신경망의 일종이다. feedforward 신경망과 달리 RNN은 내부 상태(메모리)를 사용해 입력 시퀀스를 처이할 수 있으므로 언어 번역, 주가 예측등 이전 입력을 고려해야 하는 작업에 적합하다.

RNN의 한계중 하나는 긴 문장이나 단락 등, 긴 시퀀스를 처리하는데 능숙하지 않다는 것이다.
이는 정보의 기여도가 시간이 지남에 따라 기하학적으로 감소하는 `vanishing gradient problem` 때문에 장기적인 종속성을 학습하는 것이 사실상 실질적으로 불가능하기 때문.

// 배경 지식 

@ LSTM (Long Short term memory)
LSTM은 RNN의 한 종류로서, 장기 종속성을 학습할 수 있다. RNN의 `vanishing gradient problem`을 해결하기 위해 소개되었다.
다양한 문제들을 잘 해결할 수 있고, 최근에는 널리 사용된다. RNN에 시퀀스 상에서 중요한 정보를 계속해 조정, 추적하는 역할을 하는 gate, cell state 개념을 도입함으로써 `vanishing gradient problem`을 해결했다.

@ Keras
python전용 오픈소스 신경망 네트워크 라이브러리다. TensorFlow의 위에 올라가 사용된다.

@ Tenserflow
구글에서 개발된 오픈 소스 머신 러닝 라이브러리. 파이썬으로 구축되고 cpp로 실행되는 계산 그래프를 기반으로 한다.

//

1. 데이터 표준화
input data의 스케일에 민감하므로 이를 0~1사이의 값으로 표준화한다.

표준화가 뭔지는 대충 알거고, 이걸 코드로 어떻게 표현을 하는가..

``` python
    X_normalized = (X - X_min) / (X_max - X_min)
    # 이걸 모든 범위 내의 모든 X값에 대해 실행하면 된다.
```

표준 편차를 이용하는 표준화를 사용할 수도 있음.

``` python
    X_standardized = (X - μ) / σ
    # μ : 평균, σ : 표준편차
```


2. split the data (training, testing)
시계열 데이터이므로 데이터를 시간 순으로 분할해 특정 날짜까지의 데이터를 학습에, 이후의 데이터를 테스트에 사용한다.

시계열 상의 데이터이고, 중요한 포인터들은 기억을 해야하므로 근야 무작위적으로 데이터를 쪼갤 수는 없다.

특정 시간 t 이후의 관측은 이전 관측의 종속 변수이고, 따라서 우리가 모델을 학습시킬 때

데이터의 순서가 제대로 반영되고 있는지에 주의해야 한다.



3. data를 lstm으로 변환
일정량의 시간 간격과 1개의 출력을 가진 데이터 구조를 생성한다. 이렇게 하면 training set의 각 요소에 대해 이전 훈련 training set 요소가 n개 있게 된다.

4. lstm model 빌드
Keras를 사용해 LSTM 모델을 생성한다. LSTM 레이어를 쌓고 고밀도 레이어를 추가해 출력을 생성할 수 있다.

5. 실전
모델을 사용해 주가를 예측하고 실제 가격과 비교


