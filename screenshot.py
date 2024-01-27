# 使用Python进行截屏并保存
import pyautogui

# 获取屏幕截图
img = pyautogui.screenshot()

# 保存截图
img.save('screenshot.png')

