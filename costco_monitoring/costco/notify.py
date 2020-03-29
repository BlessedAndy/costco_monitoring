'''
Created on Nov 4, 2018

@author: Andy Zhang
'''
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def send_SMS_message(message_body):
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'xxx'
    auth_token = 'xxx'
    client = Client(account_sid, auth_token)
    
    message = client.messages \
        .create(
            body = message_body,
            from_='xxx',
            to='+1xxx'
         )
    
    print(message.sid)
