#
# Regularization Methods
# Ridge and Lasso Regression
# Regulation은 loss function에 extra penalty를 추가함으로써 overfitting을 방지하는 테크닉이다.
# `penalty`는 파라미터에 대한 제한과 features/weight에 대한 표준화를 포함한다.
# 정규화 방식에 따라 regularization은 L1, L2 regularization으로 나뉜다./

# 1. Ridge Regression (L2 regularization)
# Ridge regression에서 cost function은 계수^2에 해당하는 패널티를 추가해 변경된다.
# 이러면 overfitting을 막을 수는 있지만 반대로 더 복잡하거나 유연한 모델을 학습할 때는 제약이 생김.

# 2. Lasso Regression (L1 regularization)
# Lasso (Least Absolute Shrinkage and Selection) 는
# "absolute value of magnitude"의 계수를 패널티로 loss function에 추가한다.
# 이런 유형의 정규화는 계수가 0이 될 수 있어 일부 특징이 무시될 수 있다.
# (특징 선택에도 도움이 될 수 있음)

from sklearn.linear_model import Ridge, Lasso
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import numpy as np

diabetes = load_diabetes()
x = diabetes.data
y = diabetes.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# 두 케이스 모두 alpha가 정규화 강도
# 알파값이 크면 overfitting을 줄일 수 있ㄲ지만 너무 크면 underfit이 됨
# 좋은 알파값을 선택할 것.
ridge = Ridge(alpha=1.0)
ridge.fit(x_train, y_train)

lasso = Lasso(alpha=0.1)
lasso.fit(x_train, y_train)

train_score = ridge.score(x_train, y_train)
test_score = ridge.score(x_test, y_test)

print(f"Ridge Train score: {train_score}")
print(f"Ridge Test score: {test_score}")

plt.figure(figsize=(10,6))
plt.plot(ridge.coef_, alpha=0.7, linestyle='none', marker='*', markersize=5, color='red', label=r'Ridge; $\alpha = 1.0$', zorder=7) 
plt.plot(lasso.coef_, alpha=0.5, linestyle='none', marker='d', markersize=6, color='blue', label=r'Lasso; $\alpha = 0.1$') 

plt.xlabel('Coefficient Index', fontsize=16)
plt.ylabel('Coefficient Magnitude', fontsize=16)
plt.legend(fontsize=13, loc=4)
plt.savefig("ridge.png")