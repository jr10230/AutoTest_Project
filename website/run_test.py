import unittest
from function import *
from HTMLTestReportCN import HTMLTestReportCN
import time

report_dir = './test_report/report'
test_dir = './test_case'

print("start run testcase...")
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_login.py")
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + '/' + now + 'result.html'

print("start write report...")

with open(report_name, 'wb')as f:
    runner = HTMLTestReportCN(
        stream=f,
        title="Test Report",
        description="localhost login test"
    )
    runner.run(discover)
f.close()

print("find latest report")
latest_report = latest_report(report_dir)

print("send email report..")
send_mail(latest_report)

print("test end")