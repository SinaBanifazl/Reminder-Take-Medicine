#Send SMS to MMD mail at 9:00 AM every day and remind him to use his Medicine

import smtplib, ssl
from getpass import getpass
import config
import time

smtp_server = config.SMTP_SERVER
port = config.PORT
sender_email = config.SENDER_EMAIL
password = getpass('Enter your password : ')
receiver_email = config.RECEIVER_EMAIL
message = config.MESSAGE

context = ssl.create_default_context()

medicine_time = config.MEDICINE_TIME

while True:
    current_time = time.strftime('%H:%M')
    print(f'Time : {current_time}')
    if current_time==medicine_time:
        server = smtplib.SMTP_SSL(smtp_server, port, context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print('Email sent successfully.')
        time.sleep(86400)
    else:
        print(f'Its not time to take your medicine. Please by {medicine_time}')
        time.sleep(60)

