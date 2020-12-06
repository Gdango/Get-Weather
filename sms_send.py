import os
from twilio.rest import Client

def sms_send(text_content, phone_number):

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Test!",
        from_='+13344588863',
        to=os.environ["MY_PHONE_NUMBER"]
    )
