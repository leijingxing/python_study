import face_recognition
import cv2
import numpy as np
import os

# --- 1. 准备工作 ---

# 加载已知人脸并进行编码
def load_known_faces(known_faces_dir='known_faces'):
    known_face_encodings = []
    known_face_names = []
    
    # 检查文件夹是否存在
    if not os.path.exists(known_faces_dir):
        print(f"错误：文件夹 '{known_faces_dir}' 不存在。请创建它并放入已知人脸图片。")
        return [], []

    for filename in os.listdir(known_faces_dir):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            # 加载图片
            image_path = os.path.join(known_faces_dir, filename)
            known_image = face_recognition.load_image_file(image_path)
            
            # 获取图片中的人脸编码 (假设每张图片只有一个人)
            # 如果图片中可能有多个人脸，face_encodings会返回一个列表
            encodings = face_recognition.face_encodings(known_image)
            
            if encodings:
                known_face_encoding = encodings[0]
                # 文件名作为人名 (例如: '雷军.png' -> '雷军')
                person_name = os.path.splitext(filename)[0]
                
                known_face_encodings.append(known_face_encoding)
                known_face_names.append(person_name)
                print(f"已加载 {person_name} 的人脸信息。")

    return known_face_encodings, known_face_names

# --- 2. 主程序 ---

# 从'known_faces'文件夹加载人脸数据
known_face_encodings, known_face_names = load_known_faces()

if not known_face_names:
    print("没有加载到任何已知人脸数据，程序退出。")
    exit()

# 打开摄像头 (0代表默认摄像头)
video_capture = cv2.VideoCapture(0)

# 设置摄像头分辨率（可选，可以提高性能）
# video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while True:
    # 逐帧捕获视频
    ret, frame = video_capture.read()
    if not ret:
        print("无法捕获视频帧，程序退出。")
        break

    # 为了加速处理，可以将图像缩小 (可选)
    # small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # 将图像从 BGR (OpenCV使用) 转换为 RGB (face_recognition使用)
    # rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


    # --- 核心识别流程 ---
    # 1. 查找当前帧中的所有人脸位置
    face_locations = face_recognition.face_locations(rgb_frame)
    # 2. 对找到的每个人脸进行编码
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # 3. 将当前人脸与已知人脸进行比对
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5) # tolerance越小，比对越严格
        name = "Unknown"

        # 使用欧氏距离找到最匹配的人脸
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
        
        face_names.append(name)

    # --- 4. 显示结果 ---
    # 将识别结果绘制在画面上
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # 如果之前缩小了图像，这里需要把坐标还原
        # top *= 4
        # right *= 4
        # bottom *= 4
        # left *= 4

        # 绘制人脸框
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # 绘制姓名标签
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        # 为了正确显示中文，需要更复杂的处理，这里暂时用英文演示
        # 在OpenCV中直接显示中文比较麻烦，通常需要PIL库辅助
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # 显示最终的图像
    cv2.imshow('Video', frame)

    # 按 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源并关闭所有窗口
video_capture.release()
cv2.destroyAllWindows()