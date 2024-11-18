
from mailjet_rest import Client
import os
api_key = os.environ['MJ_APIKEY_PUBLIC']
api_secret = os.environ['MJ_APIKEY_PRIVATE']
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
				{
						"From": {
								"Email": "amitbarve2003@gmail.com",
								"Name": "amit barve"
						},
						"To": [
								{
										"Email": "passenger1@mailjet.com",
										"Name": "passenger 1"
								},
								{
										"Email": "passenger2@mailjet.com",
										"Name": "passenger 2"
								}
						],
						"Cc": [
								{
										"Email": "copilot@mailjet.com",
										"Name": "Copilot"
								}
						],
						"Bcc": [
								{
										"Email": "air-traffic-control@mailjet.com",
										"Name": "Air traffic control"
								}
						],
						"Subject": "Your email flight plan!",
						"TextPart": "Dear passenger 1, welcome to Mailjet! May the delivery force be with you!",
						"HTMLPart": "<h3>Dear passenger 1, welcome to <a href=\"https://www.mailjet.com/\">Mailjet</a>!</h3><br />May the delivery force be with you!"
				}
		]
}
result = mailjet.send.create(data=data)
print result.status_code
print result.json()