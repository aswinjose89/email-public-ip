from requests import get
import smtplib, ssl
from os import path, getcwd

ip = get('https://api.ipify.org').content.decode('utf8')
path_to_file= "{}/emailip.txt".format(getcwd())
email_subject= "Existing Dubai Office Server IP"
if path.exists(path_to_file):
    f = open(path_to_file, "r")
    old_ip= f.read()
    if old_ip != ip:
        with open(path_to_file, 'w') as f:
            f.write(ip)
        email_subject= "New Dubai Office Server IP"
else:
    with open(path_to_file, 'w') as f:
        f.write(ip)
    email_subject= "New Dubai Office Server IP"

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "aswin@quantumventura.com"  # Enter your address
receiver_email = "aswin1906@gmail.com,aswinjose89@gmail.com"  # Enter receiver address
cc_email = "mktg@kayakgtl.com"
password = "put your password belongs to sender email"
message = """\
Subject: Autocreated Message By Scheduler: {}
To: {}

Kindly use the ip {} for future ssh.""".format(email_subject, receiver_email, ip)

server= smtplib.SMTP_SSL(smtp_server)
server.ehlo()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email.split(","), message)
print("Mail Sent Successfully.")