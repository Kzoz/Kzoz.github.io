import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

toaddr = ['foo@bar.us','jhon@doe.it']
cc = ['aaa@bb.com','cc@dd.com']
bcc = ['hello@world.uk']

subject = 'Email from Python Code'
fromaddr = 'your@email.com'
PASSWORD = "create a json file to store the password"
message = "\n  !! Hello... !!"

msg            = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From']    = fromaddr 
msg['To']      = ', '.join(toaddr)
msg['Cc']      = ', '.join(cc)
msg['Bcc'] = ', '.join(bcc)

# Create the body of the message (an HTML version).
text = """Hi  this is the body
"""

# Record the MIME types of both parts - text/plain and text/html.
body = MIMEText(text, 'plain')

# Attach parts into message container.
msg.attach(body)

# Send the message via local SMTP server.
s = smtplib.SMTP('server.com', 587)
s.set_debuglevel(1)
s.ehlo()
s.starttls()
s.login(fromaddr, PASSWORD)
s.sendmail(fromaddr, toaddr, msg.as_string())
s.quit()