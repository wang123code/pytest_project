import pytest


@pytest.fixture(scope="function")
def open_blog():
    print("打开blog页面_function")
