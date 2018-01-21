import time
from selenium import webdriver


#打开浏览器
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
#打开登陆页面
driver.get("http://172.31.4.74/index.php?m=user&c=public&a=login")
#输入用户名
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("yaoyao01")
#输入密码
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("123456")
#点击登录
driver.find_element_by_class_name("login_btn").click()

time.sleep(3)
#driver.find_element_by_link_text("进入商城购物").click()

driver.find_element_by_link_text("账号设置").click()
driver.find_element_by_partial_link_text("个人资料").click()
driver.find_element_by_css_selector("#true_name").clear()
driver.find_element_by_css_selector("#true_name").send_keys("小小")
driver.find_element_by_css_selector("[value=\"2\"]").click()
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
#date = driver.find_element_by_id("date")
#driver.execute_script(date.removeAttribute("readonly")
#date.clear()
#date.sendkeys("1988-01-01")

driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1988-01-01")
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("569888745")
#css中id属性前面用 #
#class属性前面 用点 .
#其他属性用[]

#保存
driver.find_element_by_css_selector(".btn4").click()
time.sleep(3)
driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()

