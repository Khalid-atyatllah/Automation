import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(email_sender, email_password, recipient_email, subject, body, smtp_server, smtp_port):
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, recipient_email, msg.as_string())

    print(f"Email sent successfully to {recipient_email}.")

