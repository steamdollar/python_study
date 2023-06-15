#
# 1. SVM : Support Vector Machine
# supervised 학습 알고리즘으로, 분류와 희귀에 사용될 수 있지만 보통 분류에 사용됨.
# SVM 알고리즘의 목표는 n차원 공간을 나누는 line 혹은 의사 결정 바운더리(decision boundary)를 생성해
# 향후 새 데이터 포인트를 쉽게 카테고리화하는 것.
# 이런 의사 결정 바운더리를 hyperplane이라고 한다.

# hyperplane에 가장 가까운 데이터 포인트/벡터를 서포트 벡터라고 한다.
# hyperplane으로부터 벡터의 거리는 margin이라고 한다.
# 목표는 가능한 큰 마진을 가진 hyperplane을 사용하는 것.

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

# visualize data
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets

iris = datasets.load_iris()
# take only two first two features
# 좀 보기 편하기 위해서 2개의 특성만 사용해 2차원 상에 plot한다.
# feature가 n개면 n차원 공간이 됨..
X = iris.data[:, :2] 
y = iris.target

# create instance of SVM and fit data
C = 1.0
clf = svm.SVC(kernel = 'linear', C=C).fit(X,y)

# create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max()+1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max()+1
h = (x_max / x_min)/100
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

plt.subplot(1,1,1)
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)


plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with linear kernel')
plt.show()

# Save the figure
plt.savefig('svm.png')

# 이건 수학적인 이해가 좀 필요할것 같음..
# n개의 특성을 가진 데이터 셋들을 n차원 공간에 뿌리고,
# 이 공간을 hyperplane으로 쪼개 classify하는 기법임.

# 1. Supprot vector
# hyperplane에 가장 가까운 데이터 포인트들로, hyper plane들의 경계가 됨.
# hyper plane은 이 서포트 벡터들이 완전히 의존하고 있으며, 서포트 벡터가 제거되면 hyperplane도 변한다.

# 2. hyperplane
# object 집단을 나누는 결정 경계. 원 데이터 공간보다 1차원 낮은 부분공간으로,
# 2차원 공간이라면 hyperplane은 1차원. (공간을 쪼개야하므로..)

# 3. margin
# 가장 가까운 클래스 포인트까지 선의 간격을 의미한다. 
# svm의 목표는 학습 데이터의 마진을 최대화 하는 최적의 hyperplane을 찾는 것이다.
# (margin이 클수록, err가 작아짐)
# 마진은 hyperplane과 두 class에서 가장 가까운 데이터 포인트 사이의 거리를 의미한다.
# 즉, 마진을 최대화한다는 것은 서로 다른 두 클래스의 가장 가까운 지점 사이의 거리를 최대화한다는 의미.

# 