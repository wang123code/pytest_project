import pytest


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
    pytest.main(['-q','test_class.py'])