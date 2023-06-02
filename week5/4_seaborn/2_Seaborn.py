#
# 1. Creating a distribution plot in Seaborn
# displot 함수를 이용해 line이 있는 히스토그램을 생성할 수 있다.
# 이 line은 Kernel Density Estimate (KDE)로 무작위 변수의 확률밀도 함수를 줌.

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# 무작위 데이터 셋 생성
data = np.random.randn(1000)

# 분포 plot을 생성
sns.distplot(data, kde=True)

plt.savefig('seaborn2.png')

#
# 2. box plot
# box plot (box-and-whicker plot)은 데이터 값의 분포를 시각적으로 묘사하는데 좋다.
# 최소값, 각 quartile, max 값들을 표현한다.

data2 = np.random.randn(1000)

sns.boxplot(data2)

plt.savefig('seaborn2_box.png')