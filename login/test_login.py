import allure
import pytest
import requests

@pytest.fixture(scope="session")
@allure.title("登录，获取token")
def test_login():
    # 公共参数
    params = {

    }
    # 参数(请求数据)
    data ={
    "loginName": "superadmin",
    "passWord": "123456"
}

    # 发送请求
    res = requests.request(
        method="POST",
        url="https://workordertest.365lawhelp.com/api/MemberAdminService/login/login",
        json=data,
    )
    # 打印相应信息
    print(res.text)
    token = "Bearer " + res.json()["data"]["token"]
    allure.attach(res.text)
    # file = open("../../Public_data/token.txt", encoding="utf-8", mode="w")
    # file.write(token)



    # 打开Excel文件
    # workbook = openpyxl.load_workbook('../excel_case/api_case_V1.xlsx')
    #
    # # 选择要操作的工作表
    # sheet = workbook['Sheet1']
    #
    # # 将值写入特定单元格
    # sheet['f2'] = "Authorization:" + token  # 将值写入A1单元格
    #
    # # 保存更改
    # workbook.save('../excel_case/api_case_V1.xlsx')
    return token
# test_login()

