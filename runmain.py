# # # pytest 自动找test_开头的测试用例
import pytest
import os
from send_email import send_test_report_email

if __name__ == '__main__':
    pytest.main(['-vs', "--alluredir", "./result", "--clean-alluredir"])
    os.system("allure generate ./result -o ./report_allure --clean")

    # 配置邮件信息
    sender_email = "1033410783@qq.com"  # 替换为发件人邮箱
    sender_password = "xluoaygcexhpbbaf"  # 替换为发件人邮箱密码
    receiver_email = "13757137493@163.com"  # 替换为收件人邮箱
    report_path = r"F:\Excel_one\report_allure\index.html"  # 替换为实际的报告路径

    if os.path.exists(report_path):
        print(f"报告文件存在，路径为: {report_path}")
        # 发送邮件
        send_test_report_email(sender_email, sender_password, receiver_email, report_path)
    else:
        print(f"报告文件不存在，路径为: {report_path}")