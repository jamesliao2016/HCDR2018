
import datetime
import json
import requests
import urllib.parse

def check_status(item_sku_id):
    # zb网站获取数据Api
    url = "http://10.180.233.104/zdm/wrapper/queryProductState?skuIdSet=" + str(item_sku_id)
    # 获取数据
    json_str = requests.get(url).text
    # json格式转为对象
    data = json.loads(json_str)
    # Info of real-time status
    return data[str(item_sku_id)]
if __name__ == '__main__':
    # print(check_status(100000243224))
    if not check_status(100000243224):
        print('stock out')