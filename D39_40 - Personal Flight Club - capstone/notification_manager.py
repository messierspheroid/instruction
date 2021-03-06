import smtplib
from twilio.rest import Client

TWILIO_SID = "ACbe414400a758cfaf10355e5bc4b53c75"
TWILIO_AUTH_TOKEN = "0c7f41a7bdfdcb9a8ded03bbbfd79f16"
TWILIO_VIRTUAL_NUMBER = "+19794646269"
TWILIO_VERIFIED_NUMBER = "+16503346124"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "bjonbergchad@gmail.com"
MY_PASSWORD = "bjornbergchad@yahoo.com"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )