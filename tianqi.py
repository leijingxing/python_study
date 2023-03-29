import requests


def get_weather_data():
    # 使用requests模块获取天气数据
    url = 'https://wttr.in/Chengdu?format=%C\n%t\n%T\n'
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    print(get_weather_data())
