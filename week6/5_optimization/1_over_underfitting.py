#
# 1. Understanding Overfitting & Underfitting
# 머신 러닝 모델을 훈련시킬때 일어나는 일반적인 현상이며,
# 좋은 모델을 개발하기 위해 매우 중요한 부분이다.


# Underfitting
# 데이터에 있는 모든 정보를 전부 캡쳐하기에는 모델이 너무 단순할 때 일어난다.
# 이 경우 모델에 bias는 크고, varinace는 작다.
# 학습 데이터에 대한 성능이 좋지 않으며(학습 데이터에 대한 오류가 높음), 
# 보이지 않는 새로운 데이터에 대한 일반화도 잘 이루어지지 않습니다.

# Overfitting
# 모델이 너무 복합할 때 (관측의 수에 비해 파라미터가 너무 많다거나) 발생한다.
# 이 경우 데이터의 기본 패턴뿐만 아니라 노이즈도 학습하기 시작해
# 학습 데이터에서는 잘 작동하지만 새로운 데이터에는 잘 일반화되지 않게 된다.

# overfitting과 underfitting 사이에서의 균형을
# Bias-Variance TradeOff 라고 한다.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

def true_fun(X):
    return np.cos(1.5 * np.pi * X)

np.random.seed(0)

n_samples = 30

# degree에 따라 model이 달라진다.
# degree = 1이면 직선, 4면 4차 함수, 15는 15차 함수
# 실제 함수는 cos 함수
degrees = [1, 4, 15]

X = np.sort(np.random.rand(n_samples))
y = true_fun(X) + np.random.randn(n_samples) * 0.1

plt.figure(figsize=(14,5))
for i in range(len(degrees)):
    ax = plt.subplot(1, len(degrees), i + 1)
    plt.setp(ax, xticks=(), yticks=())
    
    polynomial_features = PolynomialFeatures(degree=degrees[i], include_bias=False)
    linear_regression = LinearRegression()
    pipeline = Pipeline([("polynomial_features", polynomial_features), ("linear_regression", linear_regression)])
    pipeline.fit(X[:, np.newaxis], y)
    
    scores = cross_val_score(pipeline, X[:, np.newaxis], y, scoring="neg_mean_squared_error", cv=10)
    
    X_test = np.linspace(0,1,100)
    plt.plot(X_test, pipeline.predict(X_test[:, np.newaxis]), label="Model")
    plt.plot(X_test, true_fun(X_test), label="True function")
    plt.scatter(X, y, edgecolor='b', s=20, label="Samples")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim((0, 1))
    plt.ylim((-2, 2))
    plt.legend(loc="best")
    plt.title("Degree {}\nMSE = {:.2e}(+/- {:.2e})".format(degrees[i], -scores.mean(), scores.std()))
    
plt.savefig("opti.png")