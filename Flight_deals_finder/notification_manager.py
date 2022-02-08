from twilio.rest import Client

TWILIO_SID = "AC592fdffd6f2a6d7d86a36b10103eff1a"
TWILIO_AUTH_TOKEN = "a3c80c98e0a7675fffb51d1ff431ce67"
TWILIO_VIRTUAL_NUMBER = "+16066128473"
TWILIO_VERIFIED_NUMBER = "+919354162870"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
