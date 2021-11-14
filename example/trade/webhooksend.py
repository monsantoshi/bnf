import requests
import json
#webhook_url = 'http://ddfa-2001-fb1-91-765a-9136-2311-3baf-e6c6.ngrok.io'
webhook_url = 'https://mon.jprq.live'


data = 'buybnb'


r = requests.post(webhook_url, data=data)
#http://9cbf-2001-fb1-93-dcce-14c4-73c8-6ae1-4e92.ngrok.io