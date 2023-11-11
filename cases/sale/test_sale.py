from web自动化.woniusales_UI_pytest_POM.pages.sell.SellPage import SellPage
import time, allure
from PIL import ImageGrab


@allure.epic("web前端")
@allure.feature("批次管理")
@allure.story("销售出库")
class Testsale:

    def teardown_method(self):
        loging_result = rf"D:\PycharmProjects\pythonProject\web自动化\woniusales_UI_pytest_POM\screenshots\销售出库测试结果.png"
        ImageGrab.grab().save(loging_result)
        allure.attach.file(loging_result, "截图", allure.attachment_type.PNG)

    @allure.title("填写正确的信息能销售出库")
    def test_sales(self, admin_login):
        barcode = '6955203659255'
        sp = SellPage(admin_login)
        sp.assert_logout_visibility()
        sp.input_barcode(barcode)
        sp.query_click()
        sp.select_size(1)
        sp.select_paymethod(2)
        sp.input_customerphone("13541120980")
        sp.query_click2()
        sp.submit()
        sp.assert_alert("请确认你已经真实收到")
        time.sleep(2)
        sp.alert_accpet(True)
