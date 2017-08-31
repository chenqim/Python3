# 微信自动回复机器人(文字)
# coding = utf8

import requests
import itchat

TULING_TOKEN = '8a9c360b11284e30a4da16081a119038'
U_ID = 'sunnychen'

def get_message_reply_from_tuling(message_from_user):
    url_api = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': TULING_TOKEN,
        'info': message_from_user,
        'userid': U_ID,
    }
    s = requests.post(url_api, data = data).json()
    print(s)
    return s

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    reply = get_message_reply_from_tuling(msg['Text'])['text']
    itchat.send(reply, msg['FromUserName'])
    # return reply

itchat.auto_login(hotReload = True, enableCmdQR = True)
itchat.run()