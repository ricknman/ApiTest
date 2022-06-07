import allure
import pytest

from action.member_action import AdminAction
from common.red_yaml import red_yaml
from log.log import logger


@allure.feature("管理成员模块")
class TestClass():

    def setup(self):
        self.action = AdminAction()

    @allure.title("获取成员信息")
    @pytest.mark.usefixtures("int_data")
    @pytest.mark.parametrize("userid,errode,errmsg",red_yaml('get_member'))
    def test_get_member(self,userid,errode,errmsg):

        logger.info("断言开始")
        with allure.step("获取成员信息数据"):
            res = self.action.get_member(userid)
        with allure.step("断言错误码"):
            assert res["errcode"] == errode
        with allure.step("断言错误信息"):
            assert res["errmsg"] == errmsg
        logger.info("断言成功")

    @allure.title("创建成员")
    @pytest.mark.usefixtures("del_data")
    @pytest.mark.parametrize("userid,name,department,mobile,errode", red_yaml('creat_member'))
    def test_creat_member(self,userid,name,department,mobile,errode):
        res = self.action.creat_member(userid,name,department,mobile)
        assert res["errcode"] == errode
        # print(self.action.creat_member("zhangsan","张三",[1],"+86 13800000000"))

    @allure.title("更新成员信息")
    @pytest.mark.usefixtures("int_data")
    @pytest.mark.parametrize("userid,name,errcode",red_yaml('update_member'))
    def test_update_member(self,userid,name,errcode):
        res = self.action.update_member(userid,name)
        assert res["errcode"] == errcode

    @allure.title("删除成员")
    @pytest.mark.usefixtures("cret_data")
    @pytest.mark.parametrize("userid,errcode",red_yaml('delete_member'))
    def test_delete_member(self,userid,errcode):
        res = self.action.delete_member(userid)
        assert res["errcode"] == errcode


if __name__ == '__main__':
    pytest.main()