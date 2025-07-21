import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# 原始数据点
x = np.array([0.02224, 0.028334, 0.036464, 0.048068, 0.066329])
y = np.array([75, 70, 65, 60, 55])

# 创建三次样条插值函数
cs = CubicSpline(x, y, bc_type='natural')  # bc_type可以是'natural', 'clamped', 'not-a-knot'等

# 生成插值点
x_new = np.linspace(0.02, 0.07, 100)
y_new = cs(x_new)

name = ["Apollo11", "Apollo16", "Apollo17", "CE5", "CE6"]
hhh = np.array([0.06498789473684209,    0.06665315789473684,      0.060807236842105254,     0.05901671052631578,  0.06867947368421051])


# 绘制结果
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o', label='Original Data')
plt.plot(x_new, y_new, '-', label='Interpolation Curve')
plt.legend()

for i, hh in enumerate(hhh):
    th = cs(hh)
    print(name[i], " Thermal Inertia :  ", th)
    plt.scatter(hh, th,marker='+',    # 设置为加号标记
    color='red',   # 设置为红色
    s=100,         # 控制标记大小
    linewidths=2)

plt.title('H to Thermal Inertia')
plt.xlabel('H (m)', fontsize=12)  # 设置x轴标签
plt.ylabel('Thermal Inertia', fontsize=12)
plt.show()
