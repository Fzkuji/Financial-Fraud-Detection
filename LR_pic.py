import numpy as np
from matplotlib import pyplot as plt
import mpl_toolkits.axisartist as axisartist

# 创建画布
fig = plt.figure(figsize=(10, 8))
# 使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)
# 将绘图区对象添加到画布中
fig.add_axes(ax)

# 通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis[:].set_visible(False)

# ax.new_floating_axis代表添加新的坐标轴
ax.axis["x"] = ax.new_floating_axis(0, 0)
ax.axis["x"].set_axisline_style("->", size=1.5)

ax.axis["x"].label.set_text("Label")
ax.axis["x"].set_axislabel_direction("+")

ax.axis["x"].set_ticklabel_direction("+")

ax.axis["y"] = ax.new_floating_axis(1, 0)
ax.axis["y"].set_axisline_style("->", size=1.5)

ax.axis["y"].label.set_text("Label")
ax.axis["y"].set_axislabel_direction("-")

ax.axis["y"].set_ticklabel_direction("-")

x = np.arange(0, 60)
z = (x - 30) / 2
y = 1 / (1 + np.exp(-z))
plt.title("Logistics regression")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
plt.plot(x, y, label='LR')


normal_x = [4, 6, 7, 10, 15]
normal_y = [0, 0, 0.01, 0, 0.01]
plt.scatter(normal_x, normal_y, c='g', label='not fraud')

normal_x = [39, 45, 50, 53, 54, 56]
normal_y = [0.98, 0.99, 1, 0.98, 0.99, 1]
plt.scatter(normal_x, normal_y, c='r', label='fraud')

plt.vlines(30, 0, 1.1, linestyles="dashed", colors="black")
plt.hlines(0.5, -0.1, 30, linestyles="dashed", colors="black")

plt.legend(loc='center right')
plt.show()
