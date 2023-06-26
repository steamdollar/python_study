import numpy as np
import math
from sklearn.preprocessing import MinMaxScaler

def test_data(model, dataset):
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(dataset)
    
    training_data_len = math.ceil(len(dataset) * 0.8)
    
    test_data = scaled_data[training_data_len - 60:, :]
    x_test, y_test = [], dataset[training_data_len:, 3]
    
    for i in range(60, len(test_data)):
        x_test.append(test_data[i-60:i, :])
    
    x_test = np.array(x_test)
    
    predictions = model.predict(x_test)
    predictions = np.c_[np.zeros((len(predictions), 3)), predictions]
    predictions = scaler.inverse_transform(predictions)[:, 3]
    
    rmse = np.sqrt(np.mean(predictions - y_test) ** 2)
    
    return rmse