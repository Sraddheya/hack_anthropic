import smtplib
from email.mime.text import MIMEText

msg = MIMEText('Here are the best jobs we found that match your profile.')
msg['Subject'] = 'Your job alert'
msg['From'] = 'C3 jobs alert'
msg['To'] = 'ggsraddheya@gmail.com'
s = smtplib.SMTP('localhost', 1025)
s.sendmail('rohan.nittur@gmail.com', ['ggsraddheya@gmail.com'], msg.as_string())
s.quit()