import requests
import os
from bs4 import BeautifulSoup

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 遍历所有页面
for i in range(1, 50):
    url = f'http://www.netbian.com/dongwu/index_{i}.htm'
    if i == 1:
        url = f'http://www.netbian.com/dongwu'
    # 获取网页
    response = requests.get(url, headers=headers,)
    # 解析网页
    soup = BeautifulSoup(response.text, 'html.parser')
    # 获取图片标签
    img_tags = soup.find_all('img')

    # 获取图片链接
    urls = [img['src'] for img in img_tags]

# 创建文件夹
if not os.path.exists('images'):
    os.makedirs('images')

# 保存图片
for url in urls:
    filename = url.split('/')[-1]
    filepath = f'images/{filename}'
    with open(filepath, 'wb') as f:
        f.write(requests.get(url).content)

# 退出程序
exit()
