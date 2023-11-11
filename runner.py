import pytest, os

allure_result = "allure_result"
allure_report = "allure_report"
pytest.main(["-vs", "cases/batch",
             f"--alluredir={allure_result}",
             "--clean-alluredir"])

"""制作可视化报告"""
os.system(f"allure generate {allure_result} --clean -o {allure_report}")
