import pytest


def test_case4(login):
    print("用例4：登录之后，操作444\n")


def test_case5():
    print("用例5：不需要登录，操作555\n")


if __name__ == "__main__":
    pytest.main(['-s','test_fix2.py'])