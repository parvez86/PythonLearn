import imaplib
import getpass
import email

# Start the connection
M = imaplib.IMAP4_SSL('imap.gmail.com')
imaplib._MAXLINE = 10000000     # set mail text limit

# Login into the account
user = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
M.login(user,password)

# Get into the indox
M.select("inbox")       #M.list() to check the all options

typ , data = M.search(None,'SUBJECT "this is a test email for python"')

# fetching the data
result, email_data = M.fetch(data[0],"(RFC822)")
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

# Logging out
M.logout()

# Converting string to message & print it.
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)