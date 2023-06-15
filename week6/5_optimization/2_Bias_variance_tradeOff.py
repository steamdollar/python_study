#
# 2. Bias-variance TradeOff
# overfitting(high variance)과 underfitting(high bias)

# Bias
# 목표 함수를 더 쉽게 학습할 수 있도록 모델에서 만든 단순화 가정을 의미한다.
# bias가 높으면 알고리즘이 특징과 목표 출력 간 관련 관계를 놓쳐 under fitting이 일어난다.

# Variance
# 다른 학습 데이터를 사용했을 때 목표 함수의 추정치가 변경되는 양을 의미한다.
# Variance(분산)이 크면 알고리즘이 학습 데이터의 무작위 노이즈까지 모델링 해 과적합으로 이어질 수 있다.

# bias는 잘못된 가정으로 인한 오차이고, variance는 훈련 집합의 작은 변동에 대한 민감도로 인한 오차이다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error

np.random.seed(0)
n_samples = 30
true_fun = lambda X: np.cos(1.5 * np.pi * X)
X = np.sort(np.random.rand(n_samples))
y= true_fun(X) + np.random.randn(n_samples) * 0.1

degrees = np.arange(1,15)
train_error, val_error = [], []

for degree in degrees:
    polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
    linear_regression = LinearRegression()
    pipeline = Pipeline([("polynomial_features", polynomial_features), ("linear_regression", linear_regression)])
    pipeline.fit(X[:, np.newaxis], y)
    
    train_error.append(mean_squared_error(y, pipeline.predict(X[:, np.newaxis])))
    val_error.append(-cross_val_score(pipeline, X[:, np.newaxis], y, cv=10, scoring='neg_mean_squared_error').mean())

plt.plot(degrees, train_error, label='train')
plt.plot(degrees, val_error, label='cross-validation')
plt.legend(loc='upper left')
plt.xlabel('Degree')
plt.ylabel('Mean Squared Error')
plt.savefig('tradeOff.png')

# 잘 모르겠음..