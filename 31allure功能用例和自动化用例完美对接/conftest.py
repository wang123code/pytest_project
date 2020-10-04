import pytest
from selenium import webdriver
from pages.login_page import LoginPage
import time
# 上海-悠悠，QQ交流群：750815713
# 博客地址：https://www.cnblogs.com/yoyoketang/

# request 内置的fixture

@pytest.fixture(scope="session")
def driver(request):
    '''只打开浏览器和关闭浏览器'''
    driver = webdriver.Chrome()
    driver.maximize_window() # 最大化

    def end():
        print("全部用例执行完后 teardown quit dirver")
        time.sleep(5)
        driver.quit()

    request.addfinalizer(end)
    return driver

@pytest.fixture(scope="session")
def login(driver):
    web = LoginPage(driver)
    web.login()
    return driver