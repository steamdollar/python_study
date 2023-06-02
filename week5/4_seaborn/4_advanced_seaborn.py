#
# 1. Customizing Seaborn plots
# Matplotlib처럼 Seaborn도 plot을 커스터마이징 할 수 있음.

import seaborn as sns
import matplotlib.pyplot as plt

# load data set
tips = sns.load_dataset("tips")

# create a bar plot
sns.set(style="whitegrid")
bar_plot = sns.barplot(x = "day", y = "total_bill", data=tips)

# customize..
bar_plot.set_title("bar plot of total bills per day")
bar_plot.set_xlabel("Day")
bar_plot.set_ylabel("Total Bill")

plt.savefig("customize.png")

#
# 2. Facet Grids
# dataset의 feature(s)에 기반해 plot의 grid를 생성

g = sns.FacetGrid(tips, col="time", row="smoker")
g = g.map(plt.hist, "total_bill")

plt.savefig("Facet_grid.png")

#
# 3. Regression Plots
# 2개의 파라미터와 그 둘의 선형 관계를 시각화해줌..

sns.regplot(x="total_bill", y = "tip", data=tips)
plt.savefig("Regression_plots.png")