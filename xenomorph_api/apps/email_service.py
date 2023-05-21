import os
from postmark import PMMail
from dotenv import load_dotenv

load_dotenv("config/.env")

POSTMARK_API_KEY = os.getenv("POSTMARK_API_KEY")


def send_email(to, subject, body):
    try:
        print(POSTMARK_API_KEY)

        mail = PMMail(api_key=POSTMARK_API_KEY,
                      subject=subject,
                      sender="munir4303324@cloud.neduet.edu.pk",
                      to=to,
                      text_body=body)
        mail.send()
    except Exception as ex:
        ValueError(f"Error: {ex}")
