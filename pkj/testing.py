# @Time : 2020/8/11 16:20
# @Author  :小二
# @File :.py


import pytest


class TestClass:
        def test_one(self):
            x = "this"
            assert 'h' in x

        def test_two(self):
            x = "hello"
            assert hasattr(x, 'check')

        def test_three(self):
            a = "hello"
            b = "hello world"
            assert a in b


if __name__ == "__main__":
    pytest.main(['-q','test_class.py'])