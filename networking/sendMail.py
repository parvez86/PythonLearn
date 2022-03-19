import smtplib
import getpass      # for sending hide text

# Let's configure the connection
smtp_object = smtplib.SMTP('smtp.gmail.com',587)

# ehlo() command which "greets" the server and establishes the connection.
smtp_object.ehlo()

# if port 587-> TLS. Then check the connection (460 -> SSL)
smtp_object.starttls()

# login into the account
email = getpass.getpass("Enter your email: ")
password = getpass.getpass("Enter your password: ")
smtp_object.login(email,password)

# Sending mail
from_address = getpass.getpass("Enter your email: ")
to_address = getpass.getpass("Enter the email of the recipient: ")
subject = input("Enter the subject line: ")
message = input("Type out the message you want to send: ")
msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address,to_address,msg)

# Closing the connection
smtp_object.quit()