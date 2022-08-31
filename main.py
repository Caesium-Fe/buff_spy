import json
import os
import requests
import random
import datetime


# 解析json
class weaponMenu:

    # 解析json文件功能
    def __init__(self,file_path=''):
        self.file_path = file_path
        # weapon_Json 用的字段
        self.url = "url"
        self.head = "head"
        self.latest_P = "latest_price"
        self.expect_P = "expect_price"
        # 接口获取到的数据需要用的字段
        self.data = "data"
        self.items = "items"
        self.asset_info = "asset_info"
        self.lowest_bargain_price = "lowest_bargain_price"
        self.price = "price"
        self.id = "id"
        pass

    # 读取指定路径json文件
    def jsonToDict(self):
        if not os.path.exists(self.file_path):
            raise Exception("Something wrong in Json_file !")
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data_dict = json.load(f, strict=False)
        return data_dict

    # 解析weaponMenu获得url，request-head,latest—price,expect-price
    def parse_weaponMenu(self, weapon_dict):
        url = weapon_dict[self.url]
        head = weapon_dict[self.head]
        latest_price = weapon_dict[self.latest_P]
        expect_price = weapon_dict[self.expect_P]
        return url, head, latest_price, expect_price

    # 解析api接口返回的json数据获取第一条数据的bargain_price, actually_price
    def parse_itemsJson(self, api_dict):
        data = api_dict[self.data]
        items = data[self.items]
        first_item_dict = items[0]
        bargain_price = first_item_dict[self.lowest_bargain_price]
        actually_price = first_item_dict[self.price]
        return bargain_price, actually_price


# 第二个请求之间相差时间的控制模块
class inTimeSpy:

    def __init__(self):
        # 自定义随机时间范围 0到time_seed 范围内随机小数
        self.time_seed = 60
        # 获取随机时间间隔
        self.get_random_time()

    # 时间控制模块
    def get_random_time(self):
        # 获取随机秒数，让系统休眠
        i = random.uniform(0,self.time_seed)
        c = datetime.timedelta(minutes=i)
        return c


# 请求功能
class requestQuery:

    def __init__(self):
        # 完成请求功能

        pass

    def request_for_itemF(self):
        pass


# 秒杀逻辑
class secondKill:

    def __init__(self):
        # 比价功能
        pass
        # 购买功能


if __name__ == '__main__':
    json_obj = weaponMenu("weapon.json")
    json_data = json_obj.jsonToDict()
    random_seconds = inTimeSpy()
    print(random_seconds)
