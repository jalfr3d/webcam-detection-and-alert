import smtplib
from email.message import EmailMessage
import imghdr
import os

SENDER = "SENDER_EMAIL"
PASSWORD = os.getenv("PASSWORD")
RECEIVER = "RECEIVER_EMAIL"


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Movement detected in your home!"
    email_message.set_content("Hey, It's look like someone is in your house.")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()


if __name__ == "__main__":
    send_email()
