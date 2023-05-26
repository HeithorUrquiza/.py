# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC7f282388cfdf26268f0a6fa117374c78"
auth_token = "52f2e8227d786cf3fdeb0718f58ef40e"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+12542726479",
  to="+5562985002235"
)
print(message.sid)

""" from twilio.rest import Client

account_sid = 'AC7f282388cfdf26268f0a6fa117374c78'
auth_token = 'c27c7766eab0bc03bfa57c147afce0b4'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+556285002235'
)

print(message.sid) """