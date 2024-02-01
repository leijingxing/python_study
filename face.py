import cv2

# 设置要识别的图像路径
image_path = "2.jpg"

# 加载人脸识别模型
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# 读取图像
image = cv2.imread(image_path)

# 将图像转换为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 人脸检测
faces = face_cascade.detectMultiScale(gray, 1.1, 5)

# 循环遍历识别到的人脸
for (x, y, w, h) in faces:
    # 在检测到的人脸周围画框
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.putText(image, 'face', (x, y - 7), 3, 1.2, (255, 0, 0), 2, cv2.LINE_AA)

# 显示识别结果图像
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
