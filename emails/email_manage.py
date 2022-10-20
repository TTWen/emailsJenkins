# -*- coding: utf-8 -*-
# @Author  : ting.wen
# @Time    : 2022/10/18 9:50 下午
# @Function:

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailManage:
    def send_email(self, report_name):
        username = "ttwen945@gmail.com"
        password = "maoqcbmnvbxdtqlv" # 应用密码，并非邮箱登录密码
        mailfrom = username
        mailto = "qweas329@gmail.com"
        mailsubject = "hello subject"
        mailbody = "hello body"

        message = MIMEMultipart()
        message["From"] = mailfrom
        message["To"] = mailto
        message["Subject"] = mailsubject
        message.attach(MIMEText(mailbody, "plain"))


        # 当用例运行起来会生成一个测试结果的 html
        # open("test_results.htxml", "rb") 是 BinaryIO 对象
        # read() 变成字节流
        # 再添加文件格式和编码格式的参数
        message.attach(MIMEText(open(report_name, "rb").read(), "html", "utf-8"))

        # 与 Google 的 SMTP 服务器建立连接
        connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(username, password)
        connection.send_message(message)
        connection.quit()


if __name__ == '__main__':
    msg = EmailManage()
    msg.send_email()