from datetime import datetime, timedelta
import os
from twilio.rest import Client
from dotenv import load_dotenv

import time

load_dotenv()

# create a Twilio client
# Your Account SID from twilio.com/console
account_sid = "ACa3d99fad71c966d0c9dec182de747eba"
# Your Auth Token from twilio.com/console
auth_token  = "a0cfde2ed555b52d3a59ae8426e455d1"
client = Client(account_sid, auth_token)

# schedule message to be sent 61 minutes after current time
initial = datetime.utcnow()

amt = 0


send_when = datetime.utcnow() + timedelta(minutes=16)


# send the SMS
messaging_service_sid = "MG6571089e8469bbe07bda6f4c61b3bbb1"

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