#
# 1. Hierarchical Clustering : 다른 클러스터 분석 method로, 클러스터의 계층을 생성한다.
# 우선 각 개체들을 싱글톤 클러스터로 취급하고,
# 몇 개의 클러스터들은 머지가 되고, 이게 반복되어 모든 클러스터가 하나가 된다.
# 이 결과는 트리 기반의 객체 표현으로 dendrogram이라고 한다.

# Hierarchical Clustering에는 두 가지 타입이 있다.
# i) Agglomerative - 응집성 클러스터링
# bottom up 접근 방식으로, 개별 포인터에서 시작해 각 클러스터가 가장 가까운 클러스터 페어와 머지한다.

# ii) Divisive
# 탑다운 접근 방식으로, 하나의 클러스터에서 시작해 재귀적으로 쪼개진다.

# 뭘 사용할지는 상황을 고려해 결정한다.

import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# sample data
X, y = make_blobs(n_samples=50, centers=3, random_state=12)

# create agglomerative clustering model
agg_model = AgglomerativeClustering(n_clusters=3)
predicted = agg_model.fit_predict(X)

# visualize
plt.scatter(X[:, 0], X[:, 1], c=predicted)
plt.title('Agglomerative clustering')
plt.savefig('agglo_cluster.png')

# K-mean과는 다르게 scikit-learn의 Agglomerative clustering 알고리즘은
# 새로운 샘플에 대한 예측을 할 수 없으며 같은 샘플에 대한 예측과 데이터 피팅만이 가능하다.
# 이는 응집성 클러스터링의 특징에서 기인하는데, 이는 피팅하는 동안 샘플의 전체 바이너리 트리를 생성하고
# 확장성과 메모리 사용 측면에서 좋지가 않다.

# 실전에서는 데이터 구조를 고려해 method를 선택한다.
# K-mean이 데이터 수가 많을 때 계산적으로 더 빠르지만 로컬 최적값에 갖힐 수 있고,
# 초기 중심값에 따라 결과가 달라질 수 있다.
# 계츨적 클러스터링은 클러스터 수를 미리 지정할 필요가 없고, 결과 해석에 도움이 되는
# dendrogram을 제공하지만 속도가 느리고 메모리 사용이 많다.