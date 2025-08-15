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

    # 添加附件
    if os.path.exists(report_path):
        with open(report_path, "rb") as file:
            part = MIMEApplication(file.read(), Name=os.path.basename(report_path))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(report_path)}"'
        msg.attach(part)

    try:
        # 使用 SMTP_SSL 连接 QQ 邮箱 SMTP 服务器
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {e}")
        # 打印详细错误信息，便于排查问题
        import traceback
        traceback.print_exc()