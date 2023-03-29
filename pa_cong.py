import requests
from bs4 import BeautifulSoup
import pandas as pd

# 控制台输入搜索的名称
name = input('请输入搜索的名称：')
url = 'https://hanyu.baidu.com/s?wd=' + name
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
poems = soup.find_all('div', {'class': 'poem-list-item'})
data = []
for poem in poems:
    lists = poem.text.split('\n')
    print(lists)
    lists = list(filter(lambda x: x.strip(), lists))
    if len(lists) < 4:
        continue
    title = lists[0].strip()
    author = lists[1].strip() + lists[2].strip()
    content = lists[3].strip()
    data.append([title, author, content])
df = pd.DataFrame(data, columns=['Title', 'Author', 'Content'])
time = pd.Timestamp.now().strftime('%Y%m%d%H%M%S')
df.to_excel(time + '.xlsx', index=False)
# 退出程序
exit()
