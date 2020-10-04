import unittest


class Test1(unittest.TestCase):
    def test_hello(self):
        print("hello world!")


if __name__=="__main__":
    unittest.main()