#自动化测试框架unitest
import unittest

import time
from selenium import webdriver

from myTestCase import MyTestCase


class UpdataMemberInfoTest(MyTestCase):

    def test_member_updating(self):
        driver = self.driver
        print("这是一个测试用例方法,修改会员信息")
        driver.find_element_by_link_text("账号设置").click()
        driver.find_element_by_partial_link_text("个人资料").click()
        driver.find_element_by_css_selector("#true_name").clear()
        driver.find_element_by_css_selector("#true_name").send_keys("小小")
        driver.find_element_by_css_selector("[value=\"2\"]").click()
        driver.execute_script('document.getElementById("date").removeAttribute("readonly")')

        driver.find_element_by_id("date").clear()
        driver.find_element_by_id("date").send_keys("1988-01-01")
        driver.find_element_by_id("qq").clear()
        driver.find_element_by_id("qq").send_keys("569888745")
        # css中id属性前面用 #
        # class属性前面 用点 .
        # 其他属性用[]

        # 保存
        driver.find_element_by_css_selector(".btn4").click()
        time.sleep(3)
        driver.switch_to.alert.accept()
        # driver.switch_to.alert.dismiss()
    def test_denglu(self):
        driver = self.driver
        print("这是一个登陆测试")
        # 打开登陆页面
        driver.get("http://172.31.4.74/index.php?m=user&c=public&a=login")
        # 输入用户名
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("yaoyao01")
        # 输入密码
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456")
        # 点击登录
        driver.find_element_by_class_name("login_btn").click()

