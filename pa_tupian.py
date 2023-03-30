import requests
import os
from bs4 import BeautifulSoup

url = 'http://www.netbian.com/shouji/dongman/index_3.htm'
# 获取网页
response = requests.get(url)
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
