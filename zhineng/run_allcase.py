#coding=utf-8
import unittest
import os
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time
import HTMLTestRunner_jpg



def add_case(case_path,rule):
    suit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    suit.addTests(discover)
    return suit

def run_case(all_case,report_path):
    now=time.strftime("%Y_%m_%d %H_%M_%S")
    report_path=os.path.join(report_path,now+"report.html")
    runner=HTMLTestRunner_jpg.HTMLTestRunner(title="可以装逼的测试报告",description="测试结果",stream=open(report_path,"wb"),verbosity=2,retry=0)
    runner.run(all_case)


def get_report_file(report_path):
    lists=os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getatime(os.path.join(report_path,fn)))
    report_file=os.path.join(report_path,lists[-1])
    return report_file

def sent_mail(report_file,sender,receiver,psw,smtpserver,port):
    with open(report_file,"rb") as f:
        mail_body=f.read()

    msg=MIMEMultipart()
    body=MIMEText(mail_body,"html","utf-8")
    msg["Subject"]=u'自动化测试'
    msg["from"]=sender
    msg["to"]=receiver
    msg.attach(body)

    att=MIMEText(mail_body,"base64","utf-8")
    att["Content-Type"]="application/octet-stream"
    att["Content-Disposition"]='attachment;filename="report.html"'
    msg.attach(att)

    smtp=smtplib.SMTP_SSL(smtpserver,port)
    smtp.login(sender,psw)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()

if __name__ == "__main__":
    case_path = os.path.join(os.getcwd(), "case")
    rule = "test*.py"
    report_path = os.path.join(os.getcwd(), "report")
    sender = "675603318@qq.com"
    receiver= "675603318@qq.com"
    psw = 'afomahvpemypbbga'
    smtpserver = "smtp.qq.com"
    port = 465

    all_case = add_case(case_path, rule)
    run_case(all_case, report_path)
    report_file = get_report_file(report_path)
    sent_mail(report_file,sender,receiver,psw,smtpserver, port)

