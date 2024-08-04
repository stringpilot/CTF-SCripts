import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import format_datetime
from datetime import datetime, timezone

# Email configuration
smtp_server = "futuremail.ctfchallenges.net"
port = 465  # For SSL
sender_email = "as@futuremail.ctfchallenges.net"
password = "Youaresogay!"
receiver_email = "flag@futuremail.ctfchallenges.net"
subject = "Re: Flag"
body = "This is a response email sent from a Python script."

# Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
# Set the Date header to July 20, 2024, 12:00 PM GMT
future_date = datetime(2024, 8, 20, 12, 0, 0, tzinfo=timezone.utc)
message["Date"] = format_datetime(future_date)
message.attach(MIMEText(body, "plain"))

# Create a secure SSL context
context = ssl.create_default_context()

try:
    # Connect to the SMTP server using SSL
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully.")
except Exception as e:
    print(f"Error sending email: {e}")
