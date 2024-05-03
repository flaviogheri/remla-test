from flask import Flask , request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)



@app.route('/', methods =['POST '])
def predict ():
	"""
	Make a hardcoded prediction
	---
	consumes:
		- application/json
	parameters:
		- name: input_data
		  in: body
		  description: message to be classified.
		  required: True
		  schema:
		  	  type: object
			  required: sms
			  properties:
				  msg:
					  type: string
					  example: This is an example msg.
	responses:
		200:
			description: Some result
	"""
	msg = request.get_json ().get('msg')
	return {
		"result": "Message was: " + msg ,
	}

app.run(host="0.0.0.0", port =8080 , debug=True)
