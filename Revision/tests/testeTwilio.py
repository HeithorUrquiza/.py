# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
""" account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="",
  to=""
)
print(message.sid) """

from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:',
  body='Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/',
  to='whatsapp:'
)

print(message.sid)