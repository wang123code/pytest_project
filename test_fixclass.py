# @Time : 2020/8/12 16:59
# @Author  :小二


import pytest


import pytest

def setup_module():
    print("\nsetup_module：整个.py模块只执行一次")
    print("比如：所有用例开始前只打开一次浏览器")


def teardown_module():
    print("\nteardown_module：整个.py模块只执行一次")
    print("比如：所有用例结束后最后关闭浏览器")


def setup_function():
    print("\nsetup_function：每个用例开始前都会执行")


def teardown_function():
    print("teardown_function：每个用例结束后都会执行")


def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x


def test_two():
    print("正在执行----test_two")
    x = "hello"
    assert hasattr(x, 'check')


def test_three():
    print("正在执行----test_three")
    a = "hello"
    b = "hello world"
    assert a in b


class TestClass:
        def setup_method(self):
            print("\nsetup_method：类中每个用例开始前执行")

        def teardown_method(self):
            print("teardown_method：类中每个用例结束后执行")

        def setup_class(self):
            print("\nsetup_class：类中的所有用例开始前只执行一次")

        def teardown_class(self):
            print("teardown_class：类中的所有用例结束后只执行一次")

        def setup(self):
            print("setup：类中每个用例开始前执行")

        def teardown(self):
            print("teardown：类中每个用例结束后执行")

        def test_one(self):
            print("正在执行----test_one")
            x = "this"
            assert 'h' in x

        def test_two(self):
            print("正在执行----test_two")
            x = "hello"
            assert hasattr(x, 'check')

        def test_three(self):
            print("正在执行----test_three")
            a = "hello"
            b = "hello world"
            assert a in b


if __name__ == "__main__":
    pytest.main(['-q','test_fixclass.py'])
