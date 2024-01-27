# 导入模块
import requests
from bs4 import BeautifulSoup
import os

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 获取网页源代码
url = "https://desk.3gbizhi.com/"

response = requests.get(url, headers=headers)
html = response.text

# 解析网页
soup = BeautifulSoup(html, "html.parser")

# 查找图片标签
img_tags = soup.find_all("img")

# 提取图片链接
img_urls = []
for img in img_tags:
    img_url = img.get("src")
    print(img_url)
    img_urls.append(img_url)

# 创建文件夹
if not os.path.exists("img"):
    os.mkdir("img")

# 下载并保存图片
for i, img_url in enumerate(img_urls):
    # 发起网络请求，获取图片数据
    # 打开文件，以二进制写入模式
    with open(f"img/{i}.jpg", "wb") as f:
        # 写入图片数据
        f.write(requests.get(url).content)
