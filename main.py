import json
import os
import requests
import random


# 解析json
class weaponMenu:

    # 解析json文件功能
    def __init__(self,file_path=''):
        self.file_path = file_path
        self.weapon_url = None
        pass

    # 读取指定路径json文件
    def jsonToDict(self):
        if not os.path.exists(self.file_path):
            raise Exception("Something wrong in Json_file !")
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data_dict = json.load(f, strict=False)
        return data_dict

    def parse_weaponMenuJson(self, weapon_dict):
        self.weapon_url =

    def get_first_item(self, data_dict):
        data_dict =


# 实时监控系统
class inTimeSpy:

    def __init__(self, weapon_dict):
        self.random_time = None
        # 获取随机时间间隔
        self.get_random_time()

        # 时间控制模块
    def get_random_time(self):
        i = random.randint()


# 请求功能
class requestQuery:

    def __init__(self):
        # 完成请求功能
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
