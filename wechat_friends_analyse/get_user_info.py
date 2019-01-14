import itchat
import json
import requests
import codecs

sex_dict = {}
sex_dict['0'] = "其他"
sex_dict['1'] = "男"
sex_dict['2'] = "女"

message_dict = {
    "吃饭":"你想吃点啥？",
    "你好":"你好啊，这条消息是自动回复的。"
}
#下载好友头像
def download_images(frined_list):
    image_dir = "./images/"
    num = 1
    for friend in frined_list:
        image_name = str(num)+'.jpg'
        num+=1
        img = itchat.get_head_img(userName=friend["UserName"])
        with open(image_dir+image_name, 'wb') as file:
            file.write(img)
    print('头像下载完成')

def save_data(frined_list):
    out_file_name = "./data/friends.json"
    with codecs.open(out_file_name, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(frined_list,ensure_ascii=False))
    print('数据保存完成')

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    NickName = msg['User']['NickName']
    user = itchat.search_friends(name=NickName)[0]
    text = msg['Text']

    if text in message_dict.keys():
        user.send(message_dict[text])
    else:
        user.send(u"你好啊%s,我目前还不支持这个功能"%NickName)


if __name__ == '__main__':
    itchat.auto_login()
    
    friends = itchat.get_friends(update=True)[0:]#获取好友信息
    friends_list = []

    for friend in friends:
        item = {}
        item['NickName'] = friend['NickName']
        item['HeadImgUrl'] = friend['HeadImgUrl']
        item['Sex'] = sex_dict[str(friend['Sex'])]
        item['Province'] = friend['Province']
        item['Signature'] = friend['Signature']
        item['UserName'] = friend['UserName']

        friends_list.append(item)
        #print(item)

    save_data(friends_list)
    download_images(friends_list)

#    消息发送，需要将“小明”改成自己好友的名字
#    user = itchat.search_friends(name=u'小明')[0]
#    user.send(u'hello,这是一条来自机器人的消息')
#    itchat.run()
