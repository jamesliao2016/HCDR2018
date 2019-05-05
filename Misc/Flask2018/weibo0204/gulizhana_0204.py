#!/usr/bin/env python2
# coding:utf-8
# 导入相关库
import requests
from time import sleep

# 定义获取博主信息的函数
# 参数uid为博主的id

def get_user_info(uid):
    # 发送请求
    result = requests.get('https://m.weibo.cn/api/container/getIndex?type=uid&value={}'
                          .format(uid))
    json_data = result.json()  # 获取繁华信息中json内容
    json_data = json_data['data']
    userinfo = {
        'name': json_data['userInfo']['screen_name'],                    # 获取用户头像
        'description': json_data['userInfo']['description'],             # 获取用户描述
        'follow_count': json_data['userInfo']['follow_count'],           # 获取关注数
        'followers_count': json_data['userInfo']['followers_count'],     # 获取粉丝数
        'profile_image_url': json_data['userInfo']['profile_image_url'], # 获取头像
        'verified_reason': json_data['userInfo']['verified_reason'],     # 认证信息
        'containerid': json_data['tabsInfo']['tabs'][1]['containerid']   # 此字段在获取博文中需要
    }

    # 获取性别，微博中m表示男性，f表示女性
    if json_data['userInfo']['gender'] == 'm':
        gender = '男'
    elif json_data['userInfo']['gender'] == 'f':
        gender = '女'
    else:
        gender = '未知'
    userinfo['gender'] = gender
    return userinfo



# 循环获取所有博文

def get_all_post(uid, containerid):
    # 从第一页开始
    page = 0
    # 这个用来存放博文列表
    posts = []
    while True and page<10:
        # 请求博文列表
        result = requests.get('https://m.weibo.cn/api/container/getIndex?type=uid&value={}&containerid={}&page={}'
                              .format(uid, containerid, page))
        json_data = result.json()['data']

        # 当博文获取完毕，退出循环
        if not json_data['cards']:
            break

        # 循环将新的博文加入列表
        for i in json_data['cards']:
            try:
                posts.append(i['mblog']['text'])
            except:
                break

        # 停顿半秒，避免被反爬虫
        sleep(0.5)
        print(page,posts[page])

        # 跳转至下一页
        page += 1

    # 返回所有博文
    return posts

if __name__ == '__main__':
    # 获取古力娜扎信息
    userinfo = get_user_info('1350995007')
    print(userinfo)

    posts = get_all_post('1350995007', '1076031350995007')

    print(posts[:3])

    import jieba.analyse
    from html2text import html2text

    content = '\n'.join([html2text(i) for i in posts])

    # 这里使用jieba的textrank提取出1000个关键词及其比重
    result = jieba.analyse.textrank(content, topK=1000, withWeight=True)

    # 生成关键词比重字典
    keywords = dict()
    for i in result:
        keywords[i[0]] = i[1]

    from PIL import Image, ImageSequence
    import numpy as np
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud, ImageColorGenerator

    # 初始化图片
    image = Image.open('/Users/liaopeng3/code_lib/HCDR2018/miscellaneous/Flask2018/weibo0204/static/images/personas.jpg')
    graph = np.array(image)

    # 生成云图，这里需要注意的是WordCloud默认不支持中文，所以这里需要加载中文黑体字库
    wc = WordCloud(font_path='/Library/Fonts/Songti.ttc',
                   background_color='white', max_words=300, mask=graph)
    wc.generate_from_frequencies(keywords)
    image_color = ImageColorGenerator(graph)

    # 显示图片
    plt.imshow(wc)
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis("off")  # 关闭图像坐标系
    plt.show()