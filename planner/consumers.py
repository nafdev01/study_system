# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from notes.models import Certification
from planner.models import MyEvent


async def custom_save_my_event(text_data):
    try:
        name = text_data["name"]
        start_time = text_data["start_time"]
        end_time = text_data["end_time"]
        my_event = MyEvent(name=name, start_time=start_time, end_time=end_time)
        await database_sync_to_async(my_event.save)()
        return my_event
    except Exception as e:
        print(f"Error: {e}")


class NewEventConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        my_event = await custom_save_my_event(text_data_json)

        try:
            await self.send(
                text_data=json.dumps(
                    {
                        "name": my_event.name,
                        "start_time": my_event.start_time,
                        "end_time": my_event.start_time,
                    }
                )
            )
        except Exception as e:
            print(f"Error when sending reply: {e}")
