# 
# 1. Supervised Learning

# ##
# Supervised Learning에서는 feature와 label을 모두 가진 데이터셋을 가지고 있게 되며,
# 학습의 목적은 feature들이 주어졌을 때 그 대상의 label을 예측할 수 있는 estimator를 만드는 것.

# ##
# 클래스 분류를 위한 학습 알고리즘은 데이터셋의 부분 집합을 이용해 훈련된ㄷ.
# 이 경우, 주어진 feature(input)에 기반해 샘플들의 label(output)을 예측하게 되며,
# 훈련이 끝나면 모델은 새로운 (경험해보지 못한) 샘플의 class를 예측할 수 있게 된다.

# ## Common algorithm of Supervised Learning

# 1. Linear Regression(회귀) : output 변수가 실수 or 연속적인 값일 때 사용한다. (e.g. weight, temp)

# 2. Logistic Regression : output이 categorical 변수일때 사용한다. (특정 개체가 class에 속하는지 여부)

# 이 밑으로는 잘 모르겠음..

# 3. Decision Trees : classification, regression task에 사용된다. tree-like 의사결정 모델 사용

# 4. Random Forest : classification, regression 및 기타 작업을 위한 앙상블 학습 방법. 학습 시 다수의 의사 결정 트리를 구성하고, 개별 트리의 모드인 class(classification) 혹은 평균 예측 (regression)을 출력하는 방식으로 작동
# (??)

# 5. Support vector Machine : regression, classification 작업에 모두 사용되지만 보통 classfication에 사용

# 6. Naive Bayes : 예측자 간의 독립성을 가정한 Bayes' theorum에 기반한 분류 기법

#
# 2. Supervised learning in Scikit-Learn
# Scikit-learn은중간 쥬모의 supervised, unsupervised 문제를 위한 
# 광범위한 최신 머신 러닝 알고리즘을 통합하는 파이썬의 모듈이다.
# 범용 고레벨 언어를 사용해 비전문가도 머신 러닝을 사용할 수 있도록 하는데 중점을 두고 있고,
# SciPy(Scientific Python)을 기반으로 구축되었으며, scikit-learn을 사용하기 전에 설치해야 한다.

# Scikit-Learn에서 간단한 지도 학습 알고리즘을 구현하는 방법을 살펴보자.
# 여기서는 선형 회귀 모델을 예시로 사용한다.

# load library and data
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# 내장 데이터인 diabetes dataset을 사용한다.
# 특성들을 기반으로 집값을 예측할때 사용하는 데이터 셋임.
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
data = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
data['disease_progression'] = diabetes.target


# 이제 data를 attributes와 labels로 나눈다.
# 가져온 데이터셋엔 2개 column만이 있는데, bmi column을 사용해 disease_progression을 예측할 수 있다.
# LSTAT을 X, Price를 Y에 할당한다.

X = data['bmi'].values.reshape(-1,1)
y = data['disease_progression'].values.reshape(-1,1)

# data를 training set, test set으로 나눈다. 80%는 학습, 20%는 테스트에 사용한다.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# training 진행
model = LinearRegression()
model.fit(X_train, y_train)

# 훈련 이후, 예측을 진행
y_pred = model.predict(X_test)

# 예측된 값과 실제 X_test 값을 비교
df = pd.DataFrame({'Acutal' : y_test.flatten(), 'Predicted' : y_pred.flatten()})
print(df)

# Scikit-learn 라이브러리의 모델 평가는 예측의 R^2를 계산해준다.
# 점수가 1에 가까울 수록 모델이 주어진 변수로 대상 변수를 정확하게 예측할 수 있다는 것을 의미한다.
print("Training score:", model.score(X_train, y_train))
print("Test score:", model.score(X_test, y_test))

# 저 위의 train_test_split 함수에서 random_state를 바꿔주면 score가 막 달라지는데,
# 훈련 점수는 높지만 테스트 점수가 낮으면 과적합을 의미한다.
# 과적합은 모델이 노이즈, 이상값을 포함한 학습 데이터를 너무 잘 학습해
# 새로운 데이터에 대해 일반화할 수 없음을 의미한다.

# 반대로 테스트 점수가 높다는 것은 모델이 새로운 데이터에 대해 잘 예측할 수 있다는 의미 (우리 목표)