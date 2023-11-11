from web自动化.woniusales_UI_pytest_POM.pages.BasePage import BasePage


class BatchUploadPage(BasePage):
    batch_locator = "link text", "批次管理"
    batch_name_locator = "id", 'batchname'
    batch_file_locator = "id", 'batchfile'
    upload_button_locator = "xpath", '//input[@onclick="uploadBatchFile()"]'
    table_xpath_locator = "xpath", '//tbody[@id="batchinfo"]'  # 必须是xpath定位器，basepage才能拼接行
    query_locator = "id", "batchnamelist"
    query_button = "xpath", '//*[@onclick="queryBatch()"]'

    def batch_page(self):
        self.click(self.batch_locator)

    def input_batch_name(self, name):
        """输入批次名"""
        self.input_text(self.batch_name_locator, name)

    def chose_file(self, filename):
        """上传文件"""
        self.input_text(self.batch_file_locator, filename)

    def click_upload_button(self):
        """点击上传按钮"""
        self.click(self.upload_button_locator)

    def query_batch(self, index: int):
        self.select(self.query_locator, index)
        self.click(self.query_button)

    def assert_with_batch(self, text: str):
        self.assert_with_txt(self.table_xpath_locator, text)

    def assert_length(self):
        self.assert_len(self.table_xpath_locator)