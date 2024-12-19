# email sender for make it work send a email get in to your google account 
# in App passwords get the code for you app "Python"


from email.message import EmailMessage
from app2 import password
import ssl
import smtplib



email_sender = 'muradfreelancer1@gmail.com'

email_password = password
email_receiver = 'hajixa8075@ronete.com'

subject = 'your subject here'
body = """halilua halilua"""


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject 
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 535, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    




