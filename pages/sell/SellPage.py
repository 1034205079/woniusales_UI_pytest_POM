from web自动化.woniusales_UI_pytest_POM.pages.BasePage import BasePage


# 注销功能，调用BasePage里的显示等待，等待注销按钮可见
class SellPage(BasePage):
    logout_locator = "link text", '注销'
    barcode_locator = "id", "barcode"
    query_locator = "xpath", '//*[@onclick="queryByBarCode()"]'
    size_locator = "id", "goodssizeList"
    discount_locator = "xpath", '//*[@onblur="changeDiscountRatio(this)"]'
    paymethod_locator = "id", "paymethod"
    customerphone_locator = "id", "customerphone"
    query_locator2 = "xpath", '//*[@onclick="customerQueryByPhone()"]'
    submit_locator = "id", "submit"

    def assert_logout_visibility(self, timeout=5):
        """注销按钮可见"""
        self.element_should_be_visibility(self.logout_locator, timeout)

    def input_barcode(self, barcode):
        self.input_text(locator=self.barcode_locator, text=barcode, clear=True)

    def query_click(self):
        self.click(locator=self.query_locator)

    def select_size(self, index):
        self.select(locator=self.size_locator, index=index)

    def discount(self, value):
        self.javascript(locator=self.discount_locator, value=value)

    def select_paymethod(self, index):
        self.select(locator=self.paymethod_locator, index=index)

    def input_customerphone(self, phone):
        self.input_text(locator=self.customerphone_locator, text=phone, clear=True)

    def query_click2(self):
        self.click(locator=self.query_locator2)

    def submit(self):
        self.click(locator=self.submit_locator)

    def assert_alert(self, text: str):
        self.assert_witch_alter(text)

    def alert_accpet(self, accpet: bool):
        self.alert_accept_dissmiss(accpet)
