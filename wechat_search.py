import pyautogui
import time

# 启动微信
pyautogui.hotkey('alt', 'w')
pyautogui.typewrite('文件传输助手', interval=0.25)
pyautogui.press('enter')
time.sleep(3)

# 在微信中搜索好友 WeChat
pyautogui.hotkey('alt', 'tab')
pyautogui.hotkey('ctrl', 'f')

pyautogui.typewrite('文件传输助手', interval=0.25)
pyautogui.press('enter')
time.sleep(3)


# 发送消息给好友
pyautogui.click(x=100, y=100)  # 选择好友
pyautogui.typewrite('你好，这是一条自动发送的消息。', interval=0.25)
pyautogui.press('enter')