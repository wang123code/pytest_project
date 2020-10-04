import pytest
import time


def test_06(start, open_baidu):
    print("测试用例test_01")
    time.sleep(1)
    assert 1 == 2


def test_07(start, open_baidu):
    print("测试用例test_02")
    time.sleep(1)
    assert 1 == 2


if __name__ == "__main__":
    pytest.main(["-s", "test_2.py"])