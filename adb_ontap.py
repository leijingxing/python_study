import subprocess
import time

# ADB路径，根据你的实际情况修改
ADB_PATH = "adb"

# 包名
PACKAGE_NAME = "com.tshz.flutter_park"

# 获取屏幕分辨率
import re


def get_screen_resolution():
    result = subprocess.run([ADB_PATH, 'shell', 'wm', 'size'], capture_output=True, text=True)
    # 使用正则表达式提取分辨率
    match = re.search(r'(\d+)x(\d+)', result.stdout.strip())
    if match:
        width = int(match.group(1))
        height = int(match.group(2))
        return width, height
    else:
        # 如果无法匹配，抛出异常
        raise ValueError("Could not parse screen resolution from ADB output")


# 模拟点击屏幕指定坐标
def tap_screen(x, y):
    subprocess.run([ADB_PATH, 'shell', 'input', 'tap', str(x), str(y)])


# 打开应用
subprocess.run([ADB_PATH, 'shell', 'am', 'start', '-n', PACKAGE_NAME + '/.MainActivity'])

# 延迟5秒
time.sleep(5)

# 获取屏幕分辨率
width, height = get_screen_resolution()

# 计算屏幕中心点
center_x, center_y = width // 2, height // 2

# 模拟点击屏幕中间
tap_screen(center_x, center_y)