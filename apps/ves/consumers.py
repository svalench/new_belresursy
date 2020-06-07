from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from django.http import HttpResponseForbidden
globalAuto = False
globals()['autovesconn'] = globalAuto

class ChatConsumer(WebsocketConsumer):


    def connect(self):
        # a= globals()
        self.room_name = 'wert'

        if(globals()['autovesconn']==True):
            print('zaniato')
            # return 0
        else:
            self.room_group_name = 'chat_%s' % self.room_name

            globals()['autovesconn'] = True
            # Join room group
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
            self.accept()

    def disconnect(self, close_code):
        # Leave room group
        # globals()['autovesconn'] = False
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))