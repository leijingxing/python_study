from wxauto import *
import time
import pyautogui
import pyperclip

msg = '自动回复：不在'
# 获取当前微信客户端
wx = WeChat()
user = '文件传输助手'
# 获取会话列表
wx.GetSessionList()


def reply_message_if_send_key_word(user, key_word, reply_message):
    # wx.LoadRecentMessage(1)
    msgs = wx.GetAllMessage
    message_value = [msg[1] for msg in msgs]
    for index, msg in enumerate(msgs):
        if msg[1] == key_word:
            print("*" * 5)
            if reply_message not in message_value[index:]:
                print(f"收到关键词{key_word}，将自动回复以下语句:{reply_message}")
                wx.ChatWith(user)
                test = '自动回复：不在'

                def get_msg():
                    contents = test
                    return contents.split(" ")

                def send(msg):
                    pyperclip.copy(msg)
                    pyautogui.hotkey('ctrl', 'v')
                    pyautogui.press('enter')

                def send_msg(friend):
                    for i in range(1):
                        for msg in get_msg():
                            send(msg)
                            time.sleep(0.0001)

                if __name__ == '__main__':
                    send_msg(user)
            else:
                pass
            print("*" * 5)


if __name__ == '__main__':
    user = '重庆联通'
    key_word = '在吗'
    reply_message = '自动回复：不在'

    while True:
        reply_message_if_send_key_word(user=user, key_word=key_word, reply_message=reply_message)
        time.sleep(1)
