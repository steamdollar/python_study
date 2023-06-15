#
# 1. Understanding machine Learning
# 머신 러닝은 데이터 분석의 기법으로, 분석적 모델 생성을 자동화하는 것이다.
# 시스템이 데이터로부터 학습할 수 있고, 패턴을 찾아낼 수 있으며, 최소한의 인간의 개입으로
# 의사 결정을 할수 있다는 아이디어를 기반으로 한 ai의 branch이다.

# 머신 러닝 알고리즘은 다음처럼 분류된다.
# i) Supervised Learning : model이 label된 학습 데이터를 제공받으며, 
# 목표는 input (features)와 output (label)간의 관계를 학습하는 것
#
# ii) unsupervised learning : model이 unlabeled data를 제공받으며,
# 목표는 data의 내부 구조를 찾아내는 것
#
# iii) Reinforcement learning : model이 경험으로부터 행동하는 법을 배움

#
# 2. Introduction to Scikit-Learn
# Scikit-learn은 파이썬에서 가장 널리 사용되는 오픈 소스 머신 러닝 라이브러리이다.
# supervised, unsupervised 학습 알고리즘을 제공하며,
# fitting, 데이터 전처리, 모델 선택, 평가 등의 기능을 가지고 있다.

# pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn import datasets

import pandas as pd

# load dataset
iris = datasets.load_iris()
# float 타입 변수 4개를 갖는 배열들의 배열임.

# train_test_split(*arrays, **options) - dataset을 훈련 집합과 테스트 집합으로 분할하는데 사용
# 데이터를 보고, 이걸 어떤 집합에 할당할지를 무작위적으로 선택한다.
# 이렇게 되면 함수 호출마다 다른 결괏값이 나오는데,
# random_state 값을 정해주면 이 값으로 인해 분할이 항상 동일해짐.
# 난수 생성기에 맡기지 않고, 직접 난수를 정해버리는 것. 

# arrays : 동일 길이 배열들의 시퀀스 > 무작위 train, test subset으로 나뉜다.
# data는 iris 각 개체의 특성 (꽃잎 길이 등..), target은 speices를 나타냄
# test size : 제공받은 datset중 몇 퍼센트의 데이터를 사용할지 (소수면 비율, 정수면 갯수)
# random_state : 난수 생성기가 사용하는 seed - 함수 출력을 여러 실행간 일관되게 유지한다는데..
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# create a logistic regression obj
# 로지스틱 희귀 : 확률 모델 중 하나. 독립 변수의 선형 결합을 이용해 사건의 발생 가능성을 예측하는 통계 기법
# 로지스틱 희귀의 출력은 주어진 입력 포인트가 특정 class에 속할 확률이다.

# LogisticRegression class 소속 인스턴스를 생성한다. (옵션 설정 가능)
# 이 인스턴스를 이용해 내 데이터를 학습시킬 수 있음.
model = LogisticRegression(max_iter=200)

# model을 훈련시키기 위해 `fit` method를 사용한다.
# training data X_train과 training label y_train을 인수로 넣어주면 된다.
# 적당히 데이터 셋을 할당하고, 학습용 데이터를 이용해 학습시킴.
model.fit(X_train, y_train)

# model training 이후, `predict` method를 이용해
# 새로운 data의 label을 추론한다. 이 쪽도 배열 계열의 변수여야 하며 (list or DataFrame)
# 각 row는 새 data point를 위한 featrue set이다.
# output은 그 data point들에 대한 추론된 label

# 테스트 데이터에 대해 모델이 얼마나 잘 즐어맞는지를 `score` method를 통해 추론할 수 있다.
# LogisticRegression의 score method는 주어진 test data, label에 대한 평균 정확도를 나타냄.
# get model score
score = model.score(X_test, y_test)
print("model accurancy: ", score)

#
# 3. supervised vs unsupervised learning
# supervised learning에서는 주어진 이전 예제를 가지고 학습을 진행함.
# data set이 선생이고, 이 선생이 모델이나 머신을 학습시키는 역할을 한다.
# 모델이 학습을 끝마치면 새로운 데이터를 주면 추론을 진행할 수 있음
# 보통 데이터에 라벨이 지정된 경우에 사용한다.

# unsupervised learning
# 시스템이 주어진 예시로부터 바로 패턴을 찾아내려는 시도를 한다.
# 예시같은건 없고, 따라서 레이블이 지정되지 않은 데이터에서 숨겨진 구조를 스스로 찾아내는데 한계가 있다.
# 학습을 거치면 새로운 라벨을 붙일 수도 있음. (그룹을 분리한다던가 하는 작업을 거치므로)