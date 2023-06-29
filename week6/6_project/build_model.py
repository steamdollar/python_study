from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping
import os


def build_model(model_path, x_train, y_train):
    if not os.path.exists(model_path):
        # Sequential()
        # Keras method class, model의 가장 단순한 타입 (레이어들의 선형 stack)
        # .add method를 이용해 layer를 추가함으로써 Sequential model을 생성한다.
        model = Sequential()
        
        # add()
        # Sequential model에 사용하는 method. 신경만 네트워크에 layer를 추가할때 사용한다.
        # 여러 가지 레이어가 있다. LSTM layer, Dense layer, dropout layer 등등..
        # 이 레이어들은 순차적으로 쌓인다.
        
        # LSTM
        # 장기 종속성을 학습할 수 있는 뉴런 네트워크
        # 시계열, 자연어와 같은 시퀀스 데이터에 유용하다.
        model.add(LSTM(128, return_sequences=True, input_shape=(x_train.shape[1], 4)))
        model.add(LSTM(64, return_sequences=False))
        
        # Dense()
        # 이전 레이어의 모든 뉴런으로부터 각 뉴런이 입력을 받는다.
        model.add(Dense(25))
        
        # output은 4개의 뉴런을 가져야 함.
        model.add(Dense(4)) 
        
        # .compile()
        # 모델에 학습을 시작하기 전에 학습 메커니즘을 설정
        # optimizer, loss function, metrics 리스트를 매개변수로 받음.
        model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
        
        # Early stopping callback
        # 데이터 fitting 도중 발생할 수 있는 overfitting 방지
        # overfitting은 model이 패턴의 일반화를 학습하지 않고 데이터를 외우기 시작할 때 나타나는데,
        # 이러면 학습된 데이터에 대해서는 정확하지만 모르는 데이터를 정확히 예측할 수 없게 됨.
        
        # early_stopping의 메커니즘은 다음과 같다.
        # 학습하는 동안 모델의 성능은 validation dataset 
        # (실제 training에 사용되지 않은 training data의 부분집합)
        # `EarlyStopping`은 특정 metric을 모니터링한다. (보통 validation data의 loss)
        # 만약 특정 수의 epoch (`patience` 변수에 의해 결정) 동안 
        # metric이 향상되는걸 보지 못한다면 학습 종료
        
        # `restore_best_weight` 인수를 `true`로 설정하면 지표가 가장 좋았을 때의 상태로
        # revert해 갈수 있음.
        
        early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
        
        model.fit(x_train, y_train, batch_size=1, epochs=10, validation_split=0.2, callbacks=[early_stopping])
        
        model.save(model_path)
        
        return model
    else:
        model = load_model(model_path)
        
        return model