from twilio.rest import Client

# Your Twilio Account SID and Auth Token from https://www.twilio.com/console
account_sid = 'ACce63152b4d59d5ca92fa6fe56440fc95'
auth_token = '2300959509a992e22ff2185e67b8957c'

# Initialize Twilio client
client = Client(account_sid, auth_token)

def send(alert):
    try:
        # Create and send message
        message = client.messages.create(
            body=alert,
            from_='+16562211641',
            to='+917083694063'
        )
        print("################## Alert sent!")
    except Exception as e:
        print("Error sending alert:", e)
