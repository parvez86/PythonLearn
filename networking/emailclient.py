import smtplib
from email.mime.text import MIMEText

body = "This is a test email. How are you?"

msg = MIMEText(body)
msg['From'] = "alaminsrk3@gmail.com"
msg['To'] = "noonesp86@gmail.com"
msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com', 587)

# for secured connection
server.starttls()

server.login("alaminsrk3@gmail.com", "01989745377as")

server.send_message(msg)

print("Mail sent")

server.quit()

