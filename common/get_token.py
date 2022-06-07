from common.base_api import BaseApi


class GetToken(BaseApi):

    def token(self):
        # corpid = "ww5bf6bd480f360bd3"
        # corpsecret = secret
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "ww5bf6bd480f360bd3",
                "corpsecret": "DePfyCM61LzaYiDPGmiH6p43YJtq7JaYPXz5moGMssk"
            }
        }
        return self.send(**data)["access_token"]



