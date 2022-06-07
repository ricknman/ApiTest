from common.base_api import BaseApi
from common.get_token import GetToken


class AdminAction(BaseApi):

    def __init__(self):
        self.token = GetToken().token()

    def get_member(self,userid):

        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params":{
                "access_token":self.token,
                "userid":userid
            }
        }
        return self.send(**data)



    def creat_member(self,userid,name,department,mobile):

        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params":{
                "access_token":self.token
            },
            "json": {
                "userid": userid,
                "name": name,
                "department": department,
                "mobile": mobile
            }
        }
        return self.send(**data)

    def update_member(self,userid,name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/update",
            "params":{
                "access_token": self.token
            },
            "json":{
                "userid": userid,
                "name": name
            }
        }
        return self.send(**data)


    def delete_member(self,userid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params": {
                "access_token": self.token,
                "userid": userid
            }
        }
        return self.send(**data)

    def get_simplelist(self,departmentid):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/user/simplelist",
            "params": {
                "access_token": self.token,
                "department_id": departmentid
            }
        }
        return self.send(**data)