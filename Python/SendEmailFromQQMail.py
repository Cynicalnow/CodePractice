import smtplib
from email.mime.text import MIMEText
_user = "1169855719@qq.com"
_pwd = "ptgtzsjfcienjhab"
_to = "wangfei_office@126.com"
 
msg = MIMEText("Test")
msg["Subject"] = "don't panic"
msg["From"] = _user
msg["To"] = _to
 
try:
   s = smtplib.SMTP_SSL("smtp.qq.com", 465)
   s.login(_user, _pwd)
   s.sendmail(_user, _to, msg.as_string())
   s.quit()
   print ("Success!")
except smtplib.SMTPException as e:
   print ("Falied,%s"%e)
