import json
from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from . models import Client as Clients

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        # Make a database row with our channel name
        print(f'connected to  : {self.channel_name}')
        Clients.objects.create(channel_name=self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        # Note that in some rare cases (power loss, etc) disconnect may fail
        # to run; this naive example would leave zombie channel names around.
        Clients.objects.filter(channel_name=self.channel_name).delete()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.send)(self.channel_name, {
		"type": "chat.message",
		"message": message,
		})
        

    def chat_message(self, event):
        # Handles the "chat.message" event when it's sent to us.
        self.send(text_data=json.dumps({
        	'message':event["message"]
        	}))



# class ChatConsumer(AsyncWebsocketConsumer):
# 	pass
# 	async def connect(self):
# 		self.room_name = self.scope['url_route']['kwargs']['room_name']
# 		self.room_group_name  = f'chat_{self.room_name}'
# 		await self.channel_layer.group_add(
# 			self.room_group_name ,
# 			self.channel_name )
# 		# username= await self.get_username()
# 		# print(f'username : {type(username)} ')	
# 		await self.accept()
	
# 	# Database manuculation : 	
# 	@database_sync_to_async
# 	def get_username(self):
# 		return User.objects.all()[0]


# 	async def disconnect(self):
# 		await self.channel_layer.group_discard(
# 			self.room_group_name , 
# 			self.channel_name)


# 	async def receive(self , text_data):
# 		pure_data = json.loads(text_data)
# 		channel_layer = get_channel_layer()
# 		await channel_layer.send("notify", {
# 		"type": "chat.message",
# 		"text": "Hello there!",
# 		})

# 		await self.channel_layer.group_send(
# 			self.room_group_name ,
# 			{
# 				'type':'send_message',
# 				'message':pure_data['message'] 

# 			}
# 			)

# 	async def send_message(self, event):
# 		message =event['message']
		
		
# 		await self.send(
# 			text_data = json.dumps(
# 		 	{
# 			'message':message
# 			}
# 			))



	
	