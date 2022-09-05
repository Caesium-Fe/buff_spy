import json
import os
import requests
import random
import datetime


# 解析json
class WeaponMenu:

    # 解析json文件功能
    def __init__(self, file_path=''):
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
    def json_to_dict(self):
        if not os.path.exists(self.file_path):
            raise Exception("Something wrong in Json_file !")
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data_dict = json.load(f, strict=False)
        return data_dict

    # 解析weaponMenu获得url，request-head,latest—price,expect-price
    def parse_weapon_menu(self, weapon_dict):
        url = weapon_dict[self.url]
        head = weapon_dict[self.head]
        latest_price = weapon_dict[self.latest_P]
        expect_price = weapon_dict[self.expect_P]
        return url, head, latest_price, expect_price

    # 解析api接口返回的json数据获取第一条数据的bargain_price, actually_price
    def parse_items_json(self, item_json_temp):
        api_dict = json.load(item_json_temp)
        data = api_dict[self.data]
        items = data[self.items]
        first_item_dict = items[0]
        bargain_price = first_item_dict[self.lowest_bargain_price]
        actually_price = first_item_dict[self.price]
        return bargain_price, actually_price


# 第二个请求之间相差时间的控制模块
class InTimeSpy:

    def __init__(self):
        # 自定义随机时间范围 0到time_seed 范围内随机小数
        self.time_seed = 60
        # 获取随机时间间隔
        self.get_random_time()

    # 时间控制模块
    def get_random_time(self):
        # 获取随机秒数，让系统休眠
        i = random.uniform(0, self.time_seed)
        c = datetime.timedelta(minutes=i)
        return c


# 请求功能
class RequestQuery:

    def __init__(self, url, head, latest_price, expect_price):
        self.url = url
        self.head = head
        self.latest_price = latest_price
        self.expect_price = expect_price
        self.time_out = 5
        pass

    def request_for_item_f(self):
        try:
            # 完成Get请求功能
            response_obj = requests.get(url=self.url, headers=self.head, timeout=self.time_out)
            # response_obj = requests.request(method="GET", url=self.url, headers=self.head, timeout=self.time_out)
            if 200 <= response_obj.status_code < 300:
                return response_obj
            else:
                raise Exception("There is something wrong about response of " + self.url)
        except Exception as e:
            print(e)
        # pass


# 秒杀逻辑
class SecondKill:

    def __init__(self):
        # 比价功能
        pass
        # 购买功能


if __name__ == '__main__':
    json_obj = WeaponMenu("weapon.json")
    json_data = json_obj.json_to_dict()
    print(json_data)
    # 获取休眠时间
    random_seconds = InTimeSpy()
    url_t, head_t, latest_price_t, expect_price_t = json_obj.parse_weapon_menu(json_data)
    print(random_seconds)
    # 获得数据接口返回值json
    request_obj = RequestQuery(url_t, head_t, latest_price_t, expect_price_t)
    response = request_obj.request_for_item_f()
    # json转dict 看一下response.content是否为byte类型
    result = json.loads(response.content.decode('utf-8'))
    # 将json送去解析
    item_json_obj = WeaponMenu()
    # 拿到第一个item的价格和最低还价
    bargain_price_t, actually_price_t = item_json_obj.parse_items_json(item_json)
