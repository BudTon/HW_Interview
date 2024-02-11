import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class PostSend:
    def __init__(self):
        self.login_gmail = 'login@gmail.com'
        self.password = 'qwerty'
        self.subject = 'Subject'
        self.recipients = ['vasya@email.com', 'petya@email.com']
        self.message = 'Message'
        self.header = None

def send_message(GMAIL_SMTP):
    # send message
    msg = MIMEMultipart()
    msg['From'] = post.login_gmail
    msg['To'] = ', '.join(post.recipients)
    msg['Subject'] = post.subject
    msg.attach(MIMEText(post.message))
    ms = smtplib.SMTP(GMAIL_SMTP, 587)

    # identify ourselves to smtp gmail client
    ms.ehlo()

    # secure our email with tls encryption
    ms.starttls()

    # re-identify ourselves as an encrypted connection
    ms.ehlo()
    ms.login(post.login_gmail, post.password)
    ms.sendmail(post.login_gmail, ms, msg.as_string())

    ms.quit()
    # send end

def recieve(GMAIL_IMAP):
    mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
    mail.login(post.login_gmail, post.password)
    mail.list()
    mail.select("inbox")
    criterion = '(HEADER Subject "%s")' % post.header if post.header else 'ALL'
    result, data = mail.uid('search', None, criterion)
    assert data[0], 'There are no letters with current header'
    latest_email_uid = data[0].split()[-1]
    result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_string(raw_email)
    mail.logout()
    return email_message



if __name__ == '__main__':
    post = PostSend()
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"
    send_message(GMAIL_SMTP)
    print(recieve(GMAIL_IMAP))

