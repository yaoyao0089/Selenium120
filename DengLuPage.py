from selenium.webdriver.common.by import By

class LoginPage:
    #通过成员变量,保存页面元素的定位信息
    username_input_loc= (By.ID, "username")
    password_input_loc= (By.ID, "password")
    login_button_loc = (By.CLASS_NAME, "login_btn")
    url="http://172.31.4.74/index.php?m=user&c=public&a=login"

    #构造方法
    def __init__(self,driver):
        self.driver =driver
    #打开页面
    def open(self):
        self.driver.get(self.url)
     #输入用户名的方法
    def input_username(self,username):
        self.driver.find_element(*self.username_input_loc).send_keys(username)
    def input_password(self,password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)
    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()
    def login(self, username,password):
        self.open()
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()

