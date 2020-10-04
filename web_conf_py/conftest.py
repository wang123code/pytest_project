import pytest


@pytest.fixture(scope="session")
def start():
    print("\n打开浏览器")
    return "yoyo"
