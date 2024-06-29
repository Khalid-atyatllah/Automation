
import pandas as pd
from send_email import send_email
from get_smtp_server import get_smtp_server
from email_content import get_email_content

email_sender = 'your_email@gmail.com'
email_password = 'your_app_password'

excel_file = 'recipients.xlsx'

subject, body = get_email_content()

df = pd.read_excel(excel_file)

for index, row in df.iterrows():
    recipient_email = row['Email']

    smtp_server, smtp_port = get_smtp_server(recipient_email)

    send_email(email_sender, email_password, recipient_email, subject, body, smtp_server, smtp_port)

print("All emails sent successfully!")
