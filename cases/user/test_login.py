from web自动化.woniusales_UI_pytest_POM.pages.home.LoginPage import LoginPage
from web自动化.woniusales_UI_pytest_POM.pages.sell.SellPage import SellPage
from PIL import ImageGrab
import allure


# 调用登陆页面和销售页面，传入账户密码验证码，断言注销按钮
@allure.epic("web前端")
@allure.feature("用户管理")
@allure.story("登录")
class TestLogin(object):

    @allure.title("输入正确的账号能成功登录")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, browser):
        """调取页面中的功能"""
        lp = LoginPage(browser)  # 实例化的时候需要浏览器driver。
        lp.input_username("admin")
        lp.input_password("admin123")
        lp.input_verifycode("11xx")
        lp.click_login_button()
        sp = SellPage(browser)  # 实例化sell页面
        sp.assert_logout_visibility()  #

    def teardown_method(self):
        loging_result = rf"D:\PycharmProjects\pythonProject\web自动化\woniusales_UI_pytest_POM\screenshots\登录测试结果.png"
        ImageGrab.grab().save(loging_result)
        allure.attach.file(loging_result, "截图", allure.attachment_type.PNG)
