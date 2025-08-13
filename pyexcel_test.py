import pytest
import allure
from excelread import getExcel
from login.test_login import test_login
from sendhttp_test import send_requests


class TestCase:
    @allure.title("")
    @pytest.mark.parametrize('case', getExcel())
    def test_mobile(self,test_login,case):
        token = test_login
        # 从case里面拿数据
        try:
            title = case[6]  # 假设第 7 列是标题
        except IndexError:
            title = "未提供标题"  # 如果越界，使用默认标题
        allure.dynamic.title(str(title))
        url = case[1]
        data = case[2]
        method = case[3]
        params = case[4]
        headers = {"Authorization": token}
        res = send_requests(url, method, data, params, headers)
        allure.attach(res.text)



