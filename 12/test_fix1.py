import pytest


def test_case1(login):
    print("用例1：登录之后，操作111\n")


def test_case2():
    print("用例2：不需要登录，操作222\n")


def test_case3(login):
    print("用例3：登录之后，操作333\n")


if __name__ == "__main__":
    pytest.main(['-s','test_fix1.py'])