import pytest
import os
import zipfile
from send_email import send_test_report_email

if __name__ == '__main__':
    pytest.main(['-vs', "--alluredir", "./result", "--clean-alluredir"])
    os.system("allure generate ./result -o ./report_allure --clean")

    # 配置邮件信息
    sender_email = "1033410783@qq.com"  # 替换为发件人邮箱
    sender_password = "xluoaygcexhpbbaf"  # 替换为发件人邮箱密码
    receiver_email = "13757137493@163.com"  # 替换为收件人邮箱

    # 压缩 report_allure 目录
    report_dir = os.path.join(os.getcwd(), "report_allure")
    zip_file_path = os.path.join(os.getcwd(), "report_allure.zip")
    if os.path.exists(report_dir):
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(report_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, report_dir))
    else:
        print(f"报告目录不存在，路径为: {report_dir}")

    if os.path.exists(zip_file_path):
        print(f"压缩文件存在，路径为: {zip_file_path}")
        # 发送邮件
        send_test_report_email(sender_email, sender_password, receiver_email, zip_file_path)
    else:
        print(f"压缩文件不存在，路径为: {zip_file_path}")