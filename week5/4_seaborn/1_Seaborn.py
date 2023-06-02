#
# 1. Basic of Seaborn
# Matplotlib에 기반한 데이터 시각화 라이브러리.
# 통계적 데이터를 잘 시각화해 보여준다.
# Matplotlib에 이런저런 기능을 추가한 거라고 보면 됨

#
# 2. install and import
# pip install seaborn
import seaborn as sns

#
# 3. simple example
# seaborn을 이용해 간단한 scatter plot을 그려보자.
import matplotlib.pyplot as plt

# 데이터 생성
tips = sns.load_dataset("tips")

sns.scatterplot(x="total_bill", y="tip", data=tips)

plt.savefig('seaborn_1.png')