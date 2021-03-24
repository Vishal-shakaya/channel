import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
	def connect(self):
		self.accept()
		print('connected')

	def disconnect(self):
		pass

	def receive(self , text_data):
		pure_data = json.loads(text_data)
		print(pure_data)
		self.send(text_data=json.dumps(
			{
			'message':pure_data['message']
			}
			))		