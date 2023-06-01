#
# 1. Customizing Plots
# plot들을 커스터마이징 할 수 있는 여러 옵션이 있다.
# labels, titels, axes limit 등..

import matplotlib.pyplot as plt
import numpy as np

# data for plot
x = np.linspace(0,5,100)
y = np.sin(x)

# creaqte a figure and a set of subplots
fig, ax = plt.subplots()

ax.plot(x, y)


# set label and title
ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='About as simple as it gets, folks')

# set axes limit
ax.set_xlim(0,6)
ax.set_ylim(-2,2)

# display grid
ax.grid()

plt.savefig("sin.png")

#
# 2. grids, legend placement, figure size, text annotation on plot
# 격자, legend, size 조정 등을 할 수 있음.

fig, ax = plt.subplots(figsize=(8,6))

ax.plot(x,y, label='sin curve')
ax.legend(loc='upper right')
ax.grid(True)
ax.annotate('local max', xy=(1.5, 1), xytext=(3, 1.5),
arrowprops=dict(facecolor='black', shrink=0.001))

plt.savefig('sin2.png')

#
# 3. Logarithmic scale, and twinning axes
# 로그 스케일, 공유 축 사용

fig, ax1 = plt.subplots()

ax1.plot(x,y, 'b-')
ax1.set_xlabel('X')
ax1.set_ylabel('Linear scale', color='b')

# x축을 공유하는 y axis를 하나 추가
ax2 = ax1.twinx()
ax2.plot(x, np.exp(x), 'r.')
ax2.set_ylabel('Log scale', color='r')

ax2.set_yscale('log')

plt.savefig('3.png')