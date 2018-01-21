#这个类的作用, setup方法和teardown方法,从测试用例类中分离出来
#以后创建测试用例类,就不需要重新写setup和teardown方法
#原来的测试用例类 继承了unittest.TestCase类,所以需要重写setup和teardown方法
import unittest
import time
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("这个方法类似java中的beforeMethod")
        self.driver= webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self. driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        print("这个方法类似java中的afterMethod")
        time.sleep(15)
        self.driver.quit()