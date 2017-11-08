from twilio.rest import TwilioRestClient 
import pyperclip
#us per text message .0075 USD
# put your own credentials here 
ACCOUNT_SID = "ACd4f86b02aa6cab7a1464113f91b86ea7" 
AUTH_TOKEN = "12c6d141e6f61c1c23dbd970d3993f9a" 
my_number = #my number edited out
twilio_number = +16506009047
message = pyperclip.paste()
#used pyperclip to turn whatever is in my copy into a variable

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
	to=my_number, 
	from_=twilio_number, 
	body=message,  
)
