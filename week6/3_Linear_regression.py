#
# 1. Understanding Linear Regression
# 독립 변수와 종속 변수를 주어진 데이터에 기반해 모델내 변수간 관계를 선형으로 fitting하는 통계적 테크닉이다.

# Theory and Mathmatical Background
# 간단한 선형 희귀에서 종속변수(Y)는 하나의 input feature에 의해서만 예측된다.
# Y = aX + b

# 보통은 독립 변수가 여러개라고 이거의 선형 조합이 됨.
# Y = a1*X1 + a2*X2 + ... + an*Xn + b

# Code Example w/ Scikit-Learn
# Iris dataset에 대해 선형 희귀 모델을 만들어보자.

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
model = LinearRegression()
model.fit(X_train, y_train)

print("Training score : ", model.score(X_train, y_train))
print("Test score : ", model.score(X_test, y_test))