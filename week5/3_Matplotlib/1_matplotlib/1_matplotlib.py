#
# Matplotlib는 데이터를 plotting 해줄 수 있는 라이브러리.
# 1. Basics of Matplotlib
# NumPy와 자주 함께 사용된다.
# 다른 그래픽 툴킷인 PyQt, wxPython과 함께 사용되기도 한다.

# pip install matplotlib 하고
# 간단한 선형 그래프부터 만들어보자.

import matplotlib.pyplot as plt

plt.plot([0,1], [0,1])

# plot된 그래프를 저장
plt.savefig('my_figure.png')

#
# plotting the line chart

x = [ 1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]

plt.plot(x,y)

# 지금까지 plot한 모든 그래프가 표시됨.
plt.savefig('line_fig.png')

# 지금까진 plot된 데이터들을 flush
plt.clf()

#
# 3. bar chart
x = ['Apple', 'banana', "citrus", "dragonfruit"]
y = [20, 10, 30, 5]

plt.bar(x,y)
plt.savefig('bar_chart.png')

#
# 4. plotting histograms

plt.clf()

import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30)
plt.savefig("histogram.png")