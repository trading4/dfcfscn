
import json
from datetime import datetime
from time import time
import requests


spds = 'https://emrnweb.eastmoney.com/spds/Ashare.html?share_source=4&contest_finish=0&appfenxiang=1'

def encrypt(t):
    pass
    return ''

# 组合已隐藏 
# https://group.eastmoney.com/
# 隐藏查看,隐身查看

class Dfcf:
    def __init__(self):
        self.headers = {
            'User-Agent': "okhttp/3.12.13",
            'Connection': "Keep-Alive",
            'Accept': "application/json, text/plain, */*",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/json;charset=utf-8"
        }
        self.timestamp = datetime.today().__format__("%H%M%S%f")[:-3]
        self.times = int(time() * 1000)

    def list(self):
        url = "https://emdcstockcontest.dfcfs.cn/1xxxx"
        data = {
            "args": {
                "pageNum": 1,
                "pageSize": 40,
                "uid": ""
            },
            "method": "",
            "client": "",
            "disableEncrypt": '',
            "transactionId": "",
            "timestamp": '',
            "reserve": "",
            "clientType": "",
            "clientVersion": "",
            "deviceId": ""
        }
        res = requests.post(url, data=json.dumps(data), headers=self.headers).json()
        print(res)

    def hold(self):
        text = 'xxxx'
        url = 'https://emdcstockcontest.dfcfs.cn/2xxxx'
        data = {
            "args": {
                "competitionCategories": "",
                "combination": "",
                "allRecords": "",
                "pageSize": 15,
                "pageNo": 1,
                "orderSno": "",
                "bizDate": "",
                "competitionId": "",
                "startDate": "",
                "endDate": "",
                "hasLoginInfo": "",
                "uid": ""
            },
            "method": "",
            "client": "android",
            "disableEncrypt": True,
            "transactionId": '',
            "timestamp": '',
            "reserve": "",
            "clientType": "cfw",
            "clientVersion": "10.23.9",
            "deviceId": "",
            "sign": ''
        }
        res = requests.post(url, headers=self.headers, data=json.dumps(data)).json()
        print(res)


if __name__ == '__main__':
    gp = Dfcf()
    gp.hold()
