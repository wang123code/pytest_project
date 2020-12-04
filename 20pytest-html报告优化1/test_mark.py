import pytest


@pytest.mark.webtest
def test_send_http():
    '''
    这是一个web自动化测试用例
    '''
    print("mark web test")
    pass


def test_something_quick():
    pass


def test_another():
    pass


class TestMyClass:
    def test_01(self):
        print("hello :")

    def test_02(self):
        print("hello world")


if __name__ == "__main__":
    pytest.main(['-s','test_mark.py','--html=report.html','--self-contained-html'])