import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()  # 创建一个图像实例
ax = fig.add_subplot(111, projection='3d')  # 创建一个三维的绘图工程

x = np.random.standard_normal(100)  # 生成100个服从正态分布的随机数
y = np.random.standard_normal(100)  # 生成100个服从正态分布的随机数
z = np.random.standard_normal(100)  # 生成100个服从正态分布的随机数
   
ax.scatter(x, y, z)  # 绘制数据点

plt.show()  # 显示图像

