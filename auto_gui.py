from time import sleep
import pyautogui
import pyscreeze
import cv2

# 打印屏幕尺寸
print(pyautogui.size())

# 打印鼠标位置
print(pyautogui.position())

# 屏幕缩放系数 mac缩放是2 windows一般是1
screenScale = 1

# 事先读取按钮截图
target = cv2.imread(r"1.png", cv2.IMREAD_GRAYSCALE)

# 每隔5秒执行一次
while True:
    # 先截图
    screenshot = pyscreeze.screenshot('my_screenshot.png')
    # 读取图片 灰色会快
    temp = cv2.imread(r'my_screenshot.png', cv2.IMREAD_GRAYSCALE)

    theight, twidth = target.shape[:2]
    tempheight, tempwidth = temp.shape[:2]
    print("目标图宽高：" + str(twidth) + "-" + str(theight))
    print("模板图宽高：" + str(tempwidth) + "-" + str(tempheight))
    # 先缩放屏幕截图 INTER_LINEAR INTER_AREA
    scaleTemp = cv2.resize(temp, (int(tempwidth / screenScale), int(tempheight / screenScale)))
    stempheight, stempwidth = scaleTemp.shape[:2]
    print("缩放后模板图宽高：" + str(stempwidth) + "-" + str(stempheight))
    # 匹配图片
    res = cv2.matchTemplate(scaleTemp, target, cv2.TM_CCOEFF_NORMED)
    mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print("匹配度：" + str(max_val))
    if max_val >= 0.6:
        # 计算出中心点
        top_left = max_loc
        bottom_right = (top_left[0] + twidth, top_left[1] + theight)
        tagHalfW = int(twidth / 2)
        tagHalfH = int(theight / 2)
        tagCenterX = top_left[0] + tagHalfW
        tagCenterY = top_left[1] + tagHalfH
        # 左键点击屏幕上的这个位置
        pyautogui.click(tagCenterX, tagCenterY, button='left')
    else:
        print("没找到")

    # 休眠5秒
    sleep(1)

