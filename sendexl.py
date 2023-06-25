import smtplib
import os 
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import COMMASPACE
from email import encoders
from email.mime.text import MIMEText

# server="smtplib.gmail.com"
# port=587
# email_from="ieee.event2023@gmail.com"
# password="ijoqagkzrabpshsa"
# email_to=['sabarinathan.project@gmail.com','2021pecit223@gmail.com']
# subject = 'Excel File Attachment'


def techxl(server,port,email_from,password,email_to,subject):
	
	file_path="./tech.xlsx"

    
	file_name = os.path.basename(file_path)

     
	body="xl File\n\nHII"
	message = MIMEMultipart()
	message['From'] = email_from
	message['To'] = COMMASPACE.join(email_to)
	message['Subject'] = subject
	message.attach(MIMEText(body))

	with open(file_path, 'rb') as attachment:
	    excel_attachment = MIMEBase('application', 'octet-stream')
	    excel_attachment.set_payload(attachment.read())
	    encoders.encode_base64(excel_attachment)
	    excel_attachment.add_header('Content-Disposition',
	                          'attachment', filename=file_name)                       
	    message.attach(excel_attachment)

	smtpObj = smtplib.SMTP(server, port)
	smtpObj.starttls()
	smtpObj.login(email_from, password)
	smtpObj.sendmail(email_from, email_to, message.as_string())
	smtpObj.quit()

	print(f"\nThe {file_name} file has been sent to {len(email_to)} recipient(s)!")



def non_techxl(server,port,email_from,password,email_to,subject):
	file_path="./nontech.xlsx"
	file_name = os.path.basename(file_path)
 
	body="xl File"
	message = MIMEMultipart()
	message['From'] = email_from
	message['To'] = COMMASPACE.join(email_to)
	message['Subject'] = subject
	message.attach(MIMEText(body))

	with open(file_path, 'rb') as attachment:
	    excel_attachment = MIMEBase('application', 'octet-stream')
	    excel_attachment.set_payload(attachment.read())
	    encoders.encode_base64(excel_attachment)
	    excel_attachment.add_header('Content-Disposition',
	                          'attachment', filename=file_name)                       
	    message.attach(excel_attachment)

	smtpObj = smtplib.SMTP(server, port)
	smtpObj.starttls()
	smtpObj.login(email_from, password)
	smtpObj.sendmail(email_from, email_to, message.as_string())
	smtpObj.quit()

	print(f"\nThe {file_name} file has been sent to {len(email_to)} recipient(s)!")

