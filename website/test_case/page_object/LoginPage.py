from BasePage import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):
    '''首页登录页面'''
    url = "/manager/#/login"

    # 定位器
    username_loc = (By.CLASS_NAME, 'form-control.ng-pristine.ng-untouched.ng-valid.ng-empty.ng-valid-maxlength')
    password_loc = (By.CLASS_NAME, 'form-control.ng-pristine.ng-untouched.ng-valid.ng-empty')
    submit_loc = (By.ID, 'login-btn')

    def type_username(self, username):
        '''用户名输入框元素'''
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        '''密码输入框元素'''
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    def Login_action(self, username, password):
        '''测试用户名密码是否可以登录'''
        self.open()
        self.type_username(username)
        self.type_password(password)
        self.type_submit()

    loginPass_loc = (By.CLASS_NAME, "part")

    def type_loginPass_hint(self):
        return self.find_element(*self.loginPass_loc).text