from datetime import datetime, timedelta
import os
from twilio.rest import Client
from dotenv import load_dotenv

import time

load_dotenv()

# create a Twilio client
# Your Account SID from twilio.com/console
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# schedule message to be sent 61 minutes after current time
initial = datetime.utcnow()

amt = 0


send_when = datetime.utcnow() + timedelta(minutes=16)


# send the SMS
messaging_service_sid = os.getenv('TWILIO_MESSAGING_SERVICESID')

#initital message
message = client.messages \
    .create(
    from_=messaging_service_sid,
    to='+16267419957',  # ← your phone number here
    body='What is your new years resolution?',

)

#recurring message

while(amt < 4):

    sendwhen = datetime.utcnow()  + timedelta(minutes=16)

    message = client.messages.create(
        from_=messaging_service_sid,
        to='+16267419957',  # ← your phone number here
        body='Friendly reminder that you have an appointment with us next week.',
        schedule_type='fixed',
       send_at=send_when.isoformat() + 'Z',
    )

    print(message.sid)
    print(send_when)

    amt += 1

    time.sleep(16*60)
