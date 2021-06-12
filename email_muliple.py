import smtplib
import getpass
from email.mime.text import MIMEText

print("Welcome to mass mail sender")
print('Kindly Note, in case of a gmail account you need to allow login to less known apps in your google account security settings')
print("Kindly enter your email id")
sender_address=input().strip()

#password uses the getpass library
print("Note: Your password information is encrypted")
password=getpass.getpass()

print("enter the subject")
subject=input().strip()
print("enter the message, ie mail contents")
msg1=input().strip()
#server initialization
#here this value will need to be edited incase your email account is this another service provider.
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_address, password)
#draft message

def send_email(aa):
    msg=MIMEText(msg1)
    msg['Subject']=subject
    msg['From']=sender_address
    msg['To']=aa
    recipients=aa
    #in an alternate soln if you specify the recepients array in the sendemail fn call it will send it to everyone in thst list.
    server.sendmail(sender_address,recipients,msg.as_string())

print("Please enter the comma seperated list of mail ids of the recepients")
for i in input().split(','):
    send_email(i)
print("all mails sent, Thank you!")
    
