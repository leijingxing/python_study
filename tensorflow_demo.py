import cv2

# 调用opencv的函数读取图片
# 第二个参数为0表示以灰度图的形式读取
img = cv2.imread('images/fuck.jpg', 0)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()