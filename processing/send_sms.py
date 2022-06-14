from twilio.rest import Client
from celery_queues import app

class SendSMS:
    @app.task(name='sending_sms')
    def send_sms(number, message):
        client = Client('AC97792d3fc453c5c65bbad8d87c9d9e4b', '86dab6c3e2a82c6262e13d0d005969ff')
        message_twilio = client.messages \
                .create(
                     body=f"{message}",
                     from_='+19035686600',
                     to=f"+55{number}"
                 )   
        print(message_twilio.sid)