import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_test_report_email(sender_email, sender_password, receiver_email, report_path):
    try:
        # 创建邮件对象
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = '测试报告'

        # 添加邮件正文
        body = "这是测试报告，请查收。"
        msg.attach(MIMEText(body, 'plain'))

        logging.info(f"尝试添加附件，文件路径: {report_path}")
        # 添加附件
        if os.path.exists(report_path):
            try:
                with open(report_path, "rb") as file:
                    part = MIMEApplication(file.read(), _subtype="zip", Name=os.path.basename(report_path))
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(report_path)}"'
                msg.attach(part)
                logging.info("附件添加成功")
            except Exception as e:
                logging.error(f"附件添加失败: {e}", exc_info=True)
        else:
            logging.warning(f"报告文件不存在，路径为: {report_path}")

        # 连接到 SMTP 服务器并发送邮件
        logging.info(f"尝试连接 SMTP 服务器: {sender_email}")
        smtp_server = 'smtp.qq.com'
        smtp_port = 465

        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        try:
            server.login(sender_email, sender_password)
            logging.info("SMTP 登录成功")
            server.sendmail(sender_email, receiver_email, msg.as_string())
            logging.info("邮件发送成功")
        except Exception as e:
            logging.error(f"邮件发送过程中出错: {e}", exc_info=True)
        finally:
            try:
                server.quit()
                logging.info("SMTP 连接已关闭")
            except Exception as e:
                logging.error(f"关闭 SMTP 连接时出错: {e}", exc_info=True)
    except Exception as e:
        logging.error(f"邮件发送失败: {e}", exc_info=True)