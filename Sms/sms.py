from twilio.rest import Client

account_sid = "xxxxxxxx"
auth_token = "xxxxxxx"
client=Client(account_sid,auth_token)
message = client.messages.create(
        from_='xxxxxx',
        body='helloo',
        to='xxxxxx'
)
print(message.sid)