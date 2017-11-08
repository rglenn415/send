from twilio.rest import TwilioRestClient 
import pyperclip
#us per text message .0075 USD
# put your own credentials here 
ACCOUNT_SID = #edited
AUTH_TOKEN = #edited
my_number = #my number edited out
twilio_number = #edited

#used pyperclip to turn whatever is in my copy into a variable
message = pyperclip.paste()

#creates based off of API key
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
	to=my_number, 
	from_=twilio_number, 
	body=message,  
)
