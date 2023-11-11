from web自动化.woniusales_UI_pytest_POM.pages.batch_MGT.BatchPage import BatchUploadPage
import time, allure, pytest
from PIL import ImageGrab


@allure.epic("web前端")
@allure.feature("批次管理")
@allure.story("批次上传")
class TestBatch:

    @allure.title("填写正确的信息能上传成功")
    def test_upload(self, admin_login):
        file = r"C:\Users\Administrator\Desktop\testwoniusales.xls"
        batchname = 'webui' + str(time.time())[-5:]
        up = BatchUploadPage(admin_login)
        up.batch_page()
        up.input_batch_name(batchname)
        up.chose_file(file)
        up.click_upload_button()
        time.sleep(1)
        up.assert_with_batch(batchname)
        loging_result = rf"D:\PycharmProjects\pythonProject\web自动化\woniusales_UI_pytest_POM\screenshots\上传文件测试时结果.png"
        ImageGrab.grab().save(loging_result)
        allure.attach.file(loging_result, "截图", allure.attachment_type.PNG)

    @allure.title("选择正确的批次能查询到信息")
    def test_query(self, admin_login):
        time.sleep(1)
        qr = BatchUploadPage(admin_login)
        qr.batch_page()
        qr.query_batch(2)
        qr.assert_length()
        loging_result = rf"D:\PycharmProjects\pythonProject\web自动化\woniusales_UI_pytest_POM\screenshots\查询批次结果.png"
        ImageGrab.grab().save(loging_result)
        allure.attach.file(loging_result, "截图", allure.attachment_type.PNG)
