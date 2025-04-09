# 退出程序
import requests
import os
from bs4 import BeautifulSoup

# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",  # 动态生成
    "Cookie": "cf_clearance=nF_iMFMNlPPmO...",  # 浏览器完整Cookie
    "Referer": "http://www.netbian.com/qiche/",
    "Accept-Encoding": "gzip, deflate"
}

title = 'qiche'

# 遍历所有页面
urls = []
for i in range(1, 10):
    url = f'http://www.netbian.com/{title}/index_{i}.htm'
    if i == 1:
        url = f'http://www.netbian.com/{title}/'
    # 获取网页
    response = requests.get(url, headers=headers, )
    # 解析网页
    soup = BeautifulSoup(response.text, 'html.parser')
    # 获取图片标签
    img_tags = soup.find_all('img')

    # 获取图片链接
    urls += [img['src'] for img in img_tags]

# 创建文件夹
if not os.path.exists(f'{title}'):
    os.makedirs(f'{title}')

# 保存图片
for url in urls:
    filename = url.split('/')[-1]
    filepath = f'{title}/{filename}'
    with open(filepath, 'wb') as f:
        # ok: http://img.netbian.com/file/2023/1224/235849aUfrT.jpg
        # bad: http://img.netbian.com/file/2023/1224/small235849aUfrT1703433529.jpg
        # 处理图片链接 去掉small和.jpg前面10位
        url = url.replace('small', '')
        url = url[:-14] + '.jpg'
        print(url)
        f.write(requests.get(url).content)

# 退出程序

