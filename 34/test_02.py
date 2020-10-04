from selenium import webdriver
import time


def test_yoyo_02(browser:webdriver.Firefox):

    browser.get("https://blog.csdn.net/baidu_37837739")
    time.sleep(2)
    t = browser.title
    assert "汪小兴918" in t