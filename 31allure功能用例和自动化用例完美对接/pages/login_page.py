import allure


class LoginPage(Base):
    loc_用户名 = ("id", "id_username")
    loc_密码 = ("id", "id_password")
    loc_登录按钮 = ("xpath", "//*[text()='登录']")

    # 判断登录成功
    loc_后台页面 = ("xpath", "//*[text()='后台页面']")

    @allure.step("登录")
    def login(self, username="admin", password="yoyo123456"):
        '''登录'''
        self.driver.get(login_url)
        self.send(self.loc_用户名, username)
        self.send(self.loc_密码, password)
        self.click(self.loc_登录按钮)

    @allure.step("登录结果判断")
    def is_login_success(self):
        '''判断是否登录成功 True  False'''
        result = self.is_element_exist(self.loc_后台页面)
        return result