from  createXL import tech,non_tech
from sendexl import techxl,non_techxl


server="smtplib.gmail.com"
port=587
email_from=""
password=""
email_to=['']
subject = 'Excel File Attachment'


if __name__ == '__main__':
    tech()
    non_tech()
    techxl(server,port,email_from,password,email_to,subject)
    non_techxl(server,port,email_from,password,email_to,subject)
