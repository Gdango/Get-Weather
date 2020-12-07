import os
from twilio.rest import Client

def sms_send(text_content):

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=text_content,
        from_='+13344588863',
        to=os.environ["MY_PHONE_NUMBER"]
    )
