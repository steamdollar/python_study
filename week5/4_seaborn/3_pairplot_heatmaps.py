#
# 1. pair plot
# scatter plot의 매트릭스로, 데이터 셋의 각 feature들이 다른 것과 비교할 수 있다.
# diagonal plot은 일반적으로 feature의 히스토그램 or 밀도 추정을 보여준다.
# pair plot은 데이터 셋의 서로 다른 feature간의 관계를 알아보는데 유용하다.
import pandas as pd
import seaborn as sns

# pip install -U scikit-learn
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# load the iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# create pair plot
sns.pairplot(iris_df)

plt.savefig('pair_plot.png')

#
# 2. heat map
# heatmap은 각 데이터 값이 matrix에 들어있는 2차원적 그래프
# 데이터 셋들간의 관계를 확인하는데 유용하다.

import seaborn as sns
import matplotlib.pyplot as plt

corr = iris_df.corr()

sns.heatmap(corr, annot=True)

plt.savefig('heatmap.png')