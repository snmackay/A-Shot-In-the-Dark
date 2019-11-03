
from twilio.rest import Client
from flask import Flask, request, session
from twi_traverse import start, traverse
from twilio.twiml.messaging_response import MessagingResponse

account_sid = 'ACca36cc0882a359c4ccb3b73e0124627a'
auth_token = '01cc22509abf2622eb75f6f6e132c7a8'
client = Client(account_sid, auth_token)

app =Flask(__name__)
app.config.from_object(__name__)

callers = {}

@app.route("/sms", methods=['GET', 'POST'])
def reply():
	texter = request.values.get('From')
	message = ''
	if texter in callers:
		
		nodeID = callers[texter][0]
		print(request.form['Body'])
		print(callers[texter][1][nodeID])
		print('yes')
		callers[texter] = (traverse(callers[texter][1][nodeID], request.form['Body']), callers[texter][1], callers[texter][2])
		message = callers[texter][1][callers[texter][0]].dialogue
		message += "\n Actions: \n" + " | ".join(callers[texter][1][callers[texter][0]].children.keys())

	else:
		callers[texter] = start()
		message = "Welcome to A Shot in the Dark, a text based game. Note: commands are case sensitvie."
		#code to begin parsing

	response = MessagingResponse()
	response.message(message)

	return str(response)

if __name__ == '__main__':
	app.run(debug =True)