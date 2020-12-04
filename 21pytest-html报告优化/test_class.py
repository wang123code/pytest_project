import pytest
import time
from selenium import webdriver


class TestCsdn:
    def test_yoyo_01(self,browser):
        '''
        访问csdn首页
        '''
        browser.get("https://blog.csdn.net/baidu_37837739")
        time.sleep(2)
        t = browser.title
        assert "汪小兴918" == t

    def test_yoyo_02(self,browser):
        '''
        访问csdn首页
        '''
        browser.get("https://blog.csdn.net/baidu_37837739")
        time.sleep(2)
        t = browser.title
        assert "汪小兴918" in t


if __name__ == "__main__":
    pytest.main(['-s','test_class.py','--html=report.html','--self-contained-html'])