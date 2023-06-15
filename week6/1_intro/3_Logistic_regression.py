#
# 1. Understanding Logistic Regression
# 종속변수 Y가 categorical(범주형) 할 때 사용된다.
# 확률값을 반환하기 위해 로지스틱 희귀의 출력은 logistic sigmoid 함수로 변환된다.

#
# Theory and Concept
# `로지스틱 희귀`부터가 로지스틱 함수 (a.k.a sigmoid 함수)의 이름을 따서 명명됨.
# 로지스틱 함수는 모든 실수 값을 (0,1) 사이에 매핑하는 S자형 곡선 함수.
# 핵심 전제는 입력 공간을 선형 경계에 따라 각 클래스에 대해 하나씩 두 개의 영역으로 구분 할 수 있다는 것.

#
# code example w/ Scikit-Learn
# iris dataset을 로지스틱 희귀 모델을 사용해 나눠보자.

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

print("Training score:", model.score(X_train, y_train))
print("Test score : ", model.score(X_test, y_test))

# score method는 정확도를 빠르게 파악할 수 있지만,
# 실전에서는 혼동 행렬, 정밀도, 리콜 및 F1 점수등의 보다 정교한 방법을 사용해 모델의 정확도를 측정한다.

# Logistic Regression
# 로지스틱 희귀에서는 일련의 특징이 주어졌을 때 특정 클래스나 이벤트가 발생할 확률을 모델링한다.
# 선형 희귀는 출력이 연속적인 값이지만
# 로지스틱 희귀는 sigmoid 함수를 사용해 출력을 반환 
# > 두 개 이상의 불연속 class에 매핑할 수 있는 확률값을 반환한다.

# 입력 특징 벡터 X가 있고 0 or 1인 이진 출력 Y를 예측하고 싶은 상황이라고 가정하자.
# 로지스틱 희귀에선 먼저 입력 특징의 선형 조합을 취합한다.

# `z = c * 0 + c1 * x1 + ... + cn * xn`
# c가 파라미터, x가 imput feature
# 방정식 자체는 선형 희귀랑 비슷한데, z에서 차이가 있다.
# 로지스틱 희귀에서는 이 z를 sigmoid 함수에 대입해 확률 p를 얻는다.

# `p = sigmoid(z) = 1 / (1 + e^-z)`
# 이러면 p의 값은 (0,1) 의 범위 안에 있게 됨

# 그래서 이걸로 예측을 한다.
# 보통 p = 1/2 기준으로 나눠서 0.5이상이면 class1, 아니면 class0으로 예측.

# model에서 c는 일반적으로 최대 가능성 추정을 사용해 구한다.
# 학습시켜서 모델을 만든다는게 이 값들을 정하는 것.

# 로지스틱 희귀는 예측 변수가 서로 독립적이고, 출력의 로그 확률과 선형적으로 연관되어 있을 때
# 가장 잘 작동한다는 점에 유의한다.