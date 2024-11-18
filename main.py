import pandas as p
import smtplib as sm
# import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from getpass import getpass

data=p.read_excel("students.xlsx")
email_col=data.get("email")
list_of_emails=list(email_col)
print(list_of_emails)

try: 
    server=sm.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("amitbarve93@gmail.com","@mit!@#123")
    from_="amitbarve93@gmail.com"
    to_=list_of_emails
    message=MIMEMultipart("alternative")
    message['Subject']="This is just testing messge"
    message['from']="amitbarve93@gmail.com"


    html='''
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    </head>
    <body>
    <h1>This is the demo msggg</h1>
    </body>
    </html>
    
    
    '''
    text=MIMEMultipart(html,"html")
    message.attach(text)
    server.send(from_,to_,message.as_string())
    print("message has been sent to emails ")

except Exception as e:
    print(e)
s