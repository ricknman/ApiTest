
import pytest

from action.member_action import AdminAction
from common.red_yaml import red_yaml


@pytest.fixture(scope="function")
def del_data():
    """针对创建成员用例，操作完毕后删除数据"""
    pass

    yield

    userid = red_yaml('creat_member')[0][0]
    AdminAction().delete_member(userid)

@pytest.fixture(scope="function")
def int_data():
    """前置创建测试数据，后置删除测试数据"""
    data = red_yaml('creat_member')[0]
    userid, name, department, mobile = data[0], data[1], data[2], data[3]
    AdminAction().creat_member(userid,name,department,mobile)

    yield

    userid = red_yaml('creat_member')[0][0]
    AdminAction().delete_member(userid)

@pytest.fixture(scope="function")
def cret_data():
    """针对删除成员用例，前置创造测试数据"""
    data = red_yaml('creat_member')[0]
    userid, name, department, mobile = data[0], data[1], data[2], data[3]
    AdminAction().creat_member(userid,name,department,mobile)

    yield

    pass

