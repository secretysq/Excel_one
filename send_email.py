import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_test_report_email(sender_email, sender_password, receiver_email, report_path):
    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = '测试报告'

    # 添加邮件正文
    body = "这是测试报告，请查收。"
    msg.attach(MIMEText(body, 'plain'))

    print(f"尝试添加附件，文件路径: {report_path}")
    # 添加附件
    if os.path.exists(report_path):
        try:
            with open(report_path, "rb") as file:
                part = MIMEApplication(file.read(), _subtype="html", Name=os.path.basename(report_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(report_path)}"'
            msg.attach(part)
            print("附件添加成功")
        except Exception as e:
            print(f"附件添加失败: {e}")
    else:
        print(f"报告文件不存在，路径为: {report_path}")

    # 连接到 SMTP 服务器并发送邮件
    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {e}")