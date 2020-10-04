# @Time : 2020/8/13 11:39
# @Author  :小二


import pytest


@pytest.fixture(scope="module")
def login(request):
    print("\n输入账号和密码先登录")
    # 定义了三个后置函数

    def close_w1():
        print("执行teardown1!")
        print("关闭浏览器")

    def close_w2():
        print("执行teardown2!")
        print("关闭浏览器")
        raise NameError

    def close_w3():
        print("执行teardown3!")
        print("关闭浏览器")

    # 注册了三个后置函数
    request.addfinalizer(close_w1)
    request.addfinalizer(close_w2)
    request.addfinalizer(close_w3)


def test_case1(login):
    print("用例1：搜索python-1\n")


def test_case2(login):
    print("用例2：搜索python-2\n")


def test_case3(login):
    print("用例3：搜索python-3\n")


if __name__ == "__main__":
    pytest.main(['-s','test_login.py'])