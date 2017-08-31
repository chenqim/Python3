#coding = utf8

import itchat, time
from itchat.content import *

# 向文件助手发送测试消息
# itchat.auto_login(hotReload=True)
# itchat.send(u'测试消息发送', 'filehelper')

# 向自己回复自己发送的信息
'''
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(msg)
    return msg['Text']
'''

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print(msg)
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    print(msg)
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    print(msg)
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    print(msg)
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

itchat.auto_login(hotReload = True, enableCmdQR = True)
itchat.run()
