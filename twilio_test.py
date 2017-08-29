from twilio.rest import Client

account_sid = "AC407c52f60a3bae58377649eb73bbcd36"
auth_token = "52d6d9e2e2a1fe6fc8466f5cc1eba57f"

client = Client(account_sid,auth_token)

message = client.messages.create(
    to = "+2348168266619",
    from_="+23414406809",
    body = "This Dammy testing Twilio"
)

print(message.sid)