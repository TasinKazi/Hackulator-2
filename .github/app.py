import json

import os

import random

from flask import request

from twilio.rest import Client

from flask import Flask, render_template


account_sid = "AC0d25e180ed871990afef62cb4e3fe0b3"
auth_token = "20307e178e6306303e65a63a1996d1a2"

client = Client(account_sid, auth_token)



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    print(output) # This is the output that was stored in the JSON within the browser
    print(type(output))
    result = json.loads(output) #this converts the json output to a python dictionary
    print(result) # Printing the new dictionary
    print(type(result))#this shows the json converted as a python dictionary

    message = client.messages.create(
        body=result["lastname"],
        from_="+19107882522",
        to=result["firstname"]
    )
    return result

if __name__ == '__main__':
    app.run(debug=True)