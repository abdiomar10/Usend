from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'AC19b8cc4f31f210508849616cd67a1e17'
auth_token = '03f2603789ab84335fa92b01c75cdb62'
client = Client(account_sid, auth_token)

# Sending an SMS
message = client.messages.create(
    body="Hello from Twilio!",
    from_='+254713453498',  # Your Twilio number
    to='+254700524557'  # Destination number
)

print(f"Message SID: {message.sid}")
