import os

from PIL import Image
import numpy as np

"""
step:
    1. 读取图片
    2. 转换为灰度图
    3. 计算梯度
    4. 计算光源影响
    5. 重构图像
"""

a = np.asarray(Image.open('aguduo.jpg').convert('L')).astype('float')  # 打开图片并转成灰度图

depth = 10.  # (0-100)  深度值，用于调节效果
grad = np.gradient(a)  # 取图像灰度的梯度值
grad_x, grad_y = grad  # 分别取横纵图像梯度值
grad_x = grad_x * depth / 100.  # 为了使效果更明显，可以调整grad_x, grad_y的比例
grad_y = grad_y * depth / 100.  # 为了使效果更明显，可以调整grad_x, grad_y的比例
A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)  # 梯度的模
uni_x = grad_x / A  # 单位化
uni_y = grad_y / A  # 单位化
uni_z = 1. / A  # 单位化

vec_el = np.pi / 2.2  # 光源的俯视角度，弧度值
vec_az = np.pi / 4.  # 光源的方位角度，弧度值
dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x 轴的影响
dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y 轴的影响
dz = np.sin(vec_el)  # 光源对z 轴的影响

b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
b = b.clip(0, 255)  # 限制灰度值范围(0-255)

im = Image.fromarray(b.astype('uint8'))  # 重构图像
im.save('aguduoHD.jpg')  # 保存图像
os.open('aguduoHD.jpg', os.O_RDWR)  # 打开图像
os.close()  # 关闭图像
exit()  # 退出程序

