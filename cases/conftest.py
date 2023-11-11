import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefox_service
from tools.DBClass import DBClass
from web自动化.woniusales_UI_pytest_POM.pages.home.LoginPage import LoginPage
from web自动化.woniusales_UI_pytest_POM.pages.sell.SellPage import SellPage


@pytest.fixture(scope="class")
def browser():
    dr = webdriver.Firefox(service=firefox_service(log_output="firefox_log.log"))
    dr.maximize_window()
    dr.implicitly_wait(5)
    dr.get("http://192.168.12.51:8080/woniusales/")
    yield dr
    time.sleep(2)
    dr.quit()


@pytest.fixture(scope="class")
def admin_login(browser):
    lp = LoginPage(browser)  # 实例化的时候需要浏览器driver。
    lp.input_username("admin")
    lp.input_password("admin123")
    lp.input_verifycode("11xx")
    lp.click_login_button()
    sp = SellPage(browser)  # 实例化sell页面
    sp.assert_logout_visibility()  # 断言注销按钮存在
    yield sp.dr


@pytest.fixture(scope="session")
def db():
    db = DBClass(host="192.168.12.51", port=3306, user="root", password="Luoj123!@#", db="woniusales")
    yield db
