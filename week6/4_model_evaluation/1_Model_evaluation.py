#
# model의 퍼포먼스를 어떻게 평가할 것인가..
# 1. Understanding Confusion matrix
# 알고리즘의 퍼포먼스를 시각화 해주는 테이블 레이아웃.
# 행렬의 각 행은 예상 class를, 열은 실제 class를 나타낸다.

# \             Predicted No          Predicted Yes
# Actual No         TN                    FP
# Actual Yes        FN                    TP

# TP, TN은 잘 예측한거고,
# FP, FN에 주목해야 하는데,
# FP = False Positive (Type I error) : 모델이 f를 t로 잘못 예측함.
# FN = False Negative (Type II error) : 모델이 t를 f로 잘못 예측함.

from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Run classifier
classifier = LogisticRegression(max_iter=3000)
y_pred = classifier.fit(X_train, y_train).predict(X_test)

# Compute confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Plot
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)

disp = disp.plot(include_values=True,
                 cmap='viridis', ax=None, xticks_rotation='horizontal')
plt.savefig("confusion_matrix.png")