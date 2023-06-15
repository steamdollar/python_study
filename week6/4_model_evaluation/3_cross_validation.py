#
# 1. Cross Validation
# 제한된 데이터 샘플에서 머신 러닝 모델을 평가하는 데 사용되는 리샘플링 절차
# 가장 일반적인 기법은 k배 교차 검증으로, 
# 원본 샘플을 동일한 크기의 하위 샘플 k개로 무작위로 분할하는 것.
# 단일 하위 샘플은 모델 테스트를 위한 검증 데이터로 유지되고, 나머지 (k-1)개의
# 하위 샘플은 학습 데이터로 사용된다.

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

iris = load_iris()
X = iris.data
y = iris.target

clf = LogisticRegression(random_state=42, max_iter=200)

# perform 5-fold cross validation
scores = cross_val_score(clf, X, y, cv=5)

print("Cross-validation scores: ", scores)
print("Average cross-validation scores: ", scores.mean())