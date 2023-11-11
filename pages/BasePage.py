from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


# 包含一些动作，输入，点击，判断可见
class BasePage:
    def __init__(self, webdriver: WebDriver):
        self.dr = webdriver

    def input_text(self, locator, text, clear=True):
        """
        输入文本功能
        :param locator: 定位元素的方法，元祖，（“id”,"value") ("xpath","value") ("link text","value")
        :param text: 要输入的文本
        :param clear: 是否清空再输入，默认清空
        :return:None
        """
        ele = self.dr.find_element(*locator)  # 解包送入
        if clear is True:
            ele.clear()
        ele.send_keys(text)

    def click(self, locator, action_chains=False):
        """
        点击功能
        :param locator: 点击的元素定位器，元祖
        :param action_chains: 是否使用selenium内置鼠标进行点击
        :return: None
        """
        element = self.dr.find_element(*locator)
        if action_chains is True:
            ActionChains(self.dr).click(element).perform()
        else:
            element.click()

    def select(self, locator, index: int):
        ele = self.dr.find_element(*locator)
        select = Select(ele)
        select.select_by_index(index)

    def javascript(self, locator, value: str):
        ele = self.dr.find_element(*locator)
        self.dr.execute_script(f"arguments[0].setAttribute('value',{value})", ele)

    def assert_witch_alter(self, text: str):
        alert = self.dr.switch_to.alert
        assert text in alert.text

    def assert_with_txt(self, locator, text: str):
        ele = self.dr.find_element(*locator)
        assert text in ele.text

    def assert_len(self, locator):
        ele = self.dr.find_element(*locator)
        assert len(ele.text) > 0

    def alert_accept_dissmiss(self, accept=True):
        alert = self.dr.switch_to.alert
        if accept:
            alert.accept()
        else:
            alert.dismiss()

    def element_should_be_visibility(self, locator, timeout=5):
        """等待元素可见，超时时间为timeout"""
        WebDriverWait(self.dr, timeout).until(EC.visibility_of_element_located(locator))
