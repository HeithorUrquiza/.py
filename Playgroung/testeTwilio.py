# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
""" account_sid = "AC7f282388cfdf26268f0a6fa117374c78"
auth_token = "52f2e8227d786cf3fdeb0718f58ef40e"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+12542726479",
  to="+5562985002235"
)
print(message.sid) """

from twilio.rest import Client

account_sid = 'ACd36a1c0e698394be9e6695bef7d51280'
auth_token = 'a48ccce8fc751e807a1a132fec753ec9'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+556285002235'
)

print(message.sid)