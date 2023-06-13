#
# 1. UnderStanding Unsupervised Learning
# 선존재하는 라벨이 없는 데이터 셋에서 이전에는 감지되지 않았던 패턴을 인간의 개입을 최소화하며 찾아내는 것.
# 사람이 라벨링한 데이터를 사용하는 supervised learning과 달리 unsupervised learning (self-organization)은
# input에 대해 확률 밀도 함수를 허용

# unsupervised learning의 주된 methodsms cluster analysis, principal component analysis가 있다.

# i) Cluster analysis
# 데이터 포인트를 비슷한 것들끼리 여러 그룹으로 나누는 작업

# ii) Principal Component Analysis (PCA)
# PCA는 통계적인 처리 방식으로 dataset의 n개의 축을 
# 주성분으로 알려진 새로운 직교하는 n개의 축으로 변환하는 것을 의미한다.
# 관측값이 상호 연관된 여러 정량적 종속 변수에 의해 설명되는 데이터를 분석할 때 사용된다.
# 데이터에서 중요 정보를 추출후, 이 정보를 pa라고 하는 새로운 직교 변수 집합으로 표현

# K-means, DBSCAN, t-SNE 등의 알고리즘을 이용해 이를 구현한다.

from sklearn.cluster import KMeans
from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris.data

# KMeans
km = KMeans(n_clusters=3)
km.fit(X)
y_km = km.predict(X)

# plot 3 clusters
plt.scatter(
    X[y_km == 0, 0], X[y_km == 0, 1],
    s=50, c='lightgreen',
    marker='s', edgecolor='black',
    label='cluster 1'
)

plt.scatter(
    X[y_km == 1, 0], X[y_km == 1, 1],
    s=50, c='orange',
    marker='o', edgecolor='black',
    label='cluster 2'
)

plt.scatter(
    X[y_km == 2, 0], X[y_km == 2, 1],
    s=50, c='lightblue',
    marker='v', edgecolor='black',
    label='cluster 3'
)

# plot the centroids
plt.scatter(
    km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
    s=250, marker='*',
    c='red', edgecolor='black',
    label='centroids'
)
plt.legend(scatterpoints=1)
plt.grid()

plt.savefig('cluster.png')