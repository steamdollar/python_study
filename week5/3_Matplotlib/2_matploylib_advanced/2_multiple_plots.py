# subplot 함수를 사용해 동일 figure에 여러 plot을 생성할 수 있다.

import matplotlib.pyplot as plt
import numpy as np

#
# 1. Creating multiple subplots using `plt.subplots()`

# (2, 2)개의 subplot 생성
fig, axs = plt.subplots(2, 2)

# create data
x = np.linspace(0, 2 * np.pi, 100)

y1 = np.sin(x)
y2 = np.cos(x)

# plot data on each subplot
axs[0,0].plot(x, y1)
axs[0,0].set_title('sin(x)')

axs[0,1].plot(x, y2)
axs[0,1].set_title('cos(x)')

axs[1,0].plot(x, y1, 'r--')
axs[1,0].set_title('sin(x) w/ red dashed line')

axs[1,1].plot(x, y2, 'g-.')
axs[1,1].set_title('cos(x) w/ green dash-dot line')

# figure의 title 추가
fig.suptitle('Multiple plots')

# subplot 간격 조절
fig.tight_layout()

plt.savefig('multiple_plot.png')

# 
# 2. `GridSpec`을 이용해 가변성 레이아웃 subplots 만들기

from matplotlib.gridspec import GridSpec

fig = plt.figure()

# gridspec 객체 생성
gs = GridSpec(3, 3, figure=fig)

# 각 격자에 subplot 추가
ax1 = fig.add_subplot(gs[0, :])
ax1.plot(x, y1)
ax1.set_title('ax1 : Full width')

ax2 = fig.add_subplot(gs[1, :-1])
ax2.plot(x, y2)
ax2.set_title('ax2 : Height and width reduced')

ax3 = fig.add_subplot(gs[1:, -1])
ax3.plot(x, y1)
ax3.set_title('ax3 : height extended')

ax4 = fig.add_subplot(gs[-1, 0])
ax4.plot(x, y2)
ax4.set_title('ax4 : width reduced')

ax5 = fig.add_subplot(gs[-1, -2])
ax5.plot(x, y1)
ax5.set_title('ax5: Small plot')

fig.tight_layout()

#
# 3. save fig
# 파일 이름, 해상도 등을 사용할 수 있음.

plt.savefig('multiple_plot2.png', dpi=300, facecolor='gray', transparent=True)