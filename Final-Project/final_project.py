import smtplib
from mail_sender import mail_sender

sender = 'ferdi@localhost'

file_receiver = open("receiver_list.txt",'r')
data_receiver = file_receiver.read().splitlines()

file_message_text = open("message.txt",'r')
file_message_html = open("html_image.html",'r')



mail_sender = mail_sender('localhost')
mail_sender.send(sender,data_receiver,"Ini subject nya",file_message_text.read(),file_message_html.read())