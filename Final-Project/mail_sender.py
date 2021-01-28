import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class mail_sender:
    def __init__(self,server='localhost'):
        self.server = server
    
    def send(self,sender,receivers,subject,message_text='',message_html=''):
        body = "{} \n\n\n {}".format(message_text,message_html) 
        msg = MIMEMultipart()
        #msg.set_content(body)

        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ", ".join(receivers)


        plain_part = MIMEText(message_text, 'plain')
        html_part = MIMEText(message_html, 'html')
        msg.attach("README.md")

        msg.attach(plain_part)
        msg.attach(html_part)
        

        s = smtplib.SMTP(self.server)
        s.send_message(msg)
        s.quit()
        