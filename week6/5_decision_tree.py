#
# 1. Decision Tree - Theory & Concept
# 의사 결정 트리는 Supervised Machine learning의 한 타입으로,
# 데이터가 지속적으로 특정 파라미터를 기준으로 나뉘어진다.
# 의사 결정 트리는 분류와 희귀 모두에 사용되는 모델로 데이터를 분류해나가는 과정이 나무같음

# Tree는 decision node, leaves 두 개의 entity를 가진다.
# leaves는 의사 결정 or 마지막 결과물이며, decision node는 데이터가 split되는 곳이다.
# 결정은 yes/no 이지선다의 질문을 이용해 결정을 해 나가며 tree의 길을 따라간다.

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics

# 데이터 시각화를 위해 graphviz, pydot 필요

# sudo apt-get install graphviz
# pip install graphviz
import graphviz
from sklearn.tree import export_graphviz

# pip install pydot
import pydot

iris = datasets.load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

# 의사 경절트리 claassifier 생성, training data에 fit
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Accuracy : ", metrics.accuracy_score(y_test, y_pred))

# 의사 결정 과정 시각화

dot_data = export_graphviz(clf, out_file=None,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True, rounded=True,
    special_characters=True
)

(graph, ) = pydot.graph_from_dot_data(dot_data)
graph.write_png('tree.png')