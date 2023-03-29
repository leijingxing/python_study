import schedule
import time
import socket


def get_ip_address():
    # 获取本机IP地址
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def job():
    print(get_ip_address())


if __name__ == '__main__':
    schedule.every().hour.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
