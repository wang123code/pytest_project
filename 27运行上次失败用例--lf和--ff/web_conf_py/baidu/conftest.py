import pytest


@pytest.fixture(scope="session")
def open_baidu():
    print("打开百度页面_session")