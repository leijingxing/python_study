import cv2
from PIL import Image

# 加载两张图片（原始图像和目标图像）
image1 = Image.open('original_face.jpg')
image2 = Image.open('target_face.jpg')

# 将PIL格式转为OpenCV格式
cv_img1 = cv2.cvtColor(np.array(image1), cv2.COLOR_RGB2BGR)
cv_img2 = cv2.cvtColor(np.array(image2), cv2.COLOR_RGB2BGR)

# 创建人脸对齐器
aligner = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# 定位并提取特征点
faces1 = aligner(cv_img1)
faces2 = aligner(cv_img2)
points1 = []
for face in faces1:
    shape = predictor(cv_img1, face)
    points1.append([(shape.part(i).x, shape.part(i).y) for i in range(0, 68)])
points2 = []
for face in faces2:
    shape = predictor(cv_img2, face)
    points2.append([(shape.part(i).x, shape.part(i).y) for i in range(0, 68)])

# 计算变形参数
warp_matrix = cv2.estimateAffinePartial2D(np.float32(points1[0]), np.float32(points2[0]))

# 应用变形参数到第二张图片上
result = cv2.warpAffine(cv_img2, warp_matrix, (image2.width, image2.height))

# 显示结果
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(cv_img1, cv2.COLOR_BGR2RGB))
plt.title('Original Face')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title('Swapped Face')
plt.axis('off')
plt.show()