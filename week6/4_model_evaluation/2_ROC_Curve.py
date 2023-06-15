#
# 1. ROC Curve (Receiver Operating Characteristic)
# 판별 임계값이 변할 때 이진 분류기의 성능을 보여주는 그래픽 플롯
# 이 곡선은 다양한 임계값 설정에서 FP rate에 대한 tp rate를 그래프로 표시해 만들어진다.
# 곡선 아래 면적 (AUC-ROC)는 파라미터가 
# 두 그룹(에러, 정상)을 얼마나 잘 구분할 있는지 나타내는 척도가 된다.

from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# Load the breast cancer dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a classifier and make predictions
clf = LogisticRegression(max_iter=3000)
clf.fit(X_train, y_train)
y_score = clf.predict_proba(X_test)[:,1]

# Compute ROC curve and ROC area
fpr, tpr, _ = roc_curve(y_test, y_score)
roc_auc = auc(fpr, tpr)

# Plot ROC curve
plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange', lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic Example')
plt.legend(loc="lower right")
plt.savefig('roc.png')