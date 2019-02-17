# coding = utf-8

# This is a unittest demo

import unittest

#创建一个最简单的加法函数
def add(x, y):
    return x + y


class Demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        print()

    def test_demo(self):
        print("My first unit unit test demo")
        self.assertEqual(add(10,1),11,"assert equal") # 失败时，msg会打出来

    def test_demo2(self):
        print("My second unit unit test demo")
        self.assertEqual(add(10,1),11,"assert equal") # 失败时，msg会打出来

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")




