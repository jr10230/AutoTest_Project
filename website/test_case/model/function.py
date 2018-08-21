import smtplib   # 发送邮件模块
from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header
import os


def insert_img(driver, filename):
    '''截图'''
    func_path = os.path.dirname(__file__)
    base_dir = str(func_path)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/website')[0]
    filepath = base + '/website/test_report/screenshot/' + filename
    driver.get_screenshot_as_file(filepath)


def send_mail(latest_report):
    '''发送邮件'''
    f = open(latest_report, 'rb')
    mail_content = f.read()
    f.close()

    smtpserver = 'smtp.163.com'

    user = '17709014589@163.com'
    password = 'yyygo20'

    sender = '17709014589@163.com'
    receives = ['906193135@qq.com', '2067513208@qq.com']

    subject = 'Web Selenium 自动化测试报告'

    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = ','.join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    # print("Start send email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    # print("Send email end!")


def latest_report(report_dir):
    '''查看最新测试报告'''
    lists = os.listdir(report_dir)
    # print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    # print("The latest report is " + lists[-1])

    file = os.path.join(report_dir, lists[-1])
    # print(file)
    return file