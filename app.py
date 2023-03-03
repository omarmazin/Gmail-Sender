# ライブラリ : smtplib, ssl, EmailMessage
# 
import data
import smtplib
import ssl
from email.message import EmailMessage

e_sender = data.my_email
e_password = data.my_password
target = data.receivers

subject = 'アプリのテスト'
body = """
このメッセージはテストの結果です!
"""

em = EmailMessage()
em['From'] = e_sender
em['To'] = target
em['Cc'] = "cc@cc.com"
em['Subject'] = subject
em.set_content(body)
context = ssl.create_default_context()

try:

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(e_sender, e_password)
        smtp.sendmail(e_sender, target, em.as_string())
        print("Done!")
except:
    print("error, Try to generate password from gmail => security => App Passwords => Custome => Generate => then use it instead your default password (;")