# consumers.py
import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from accounts.models import Student
from notes.models import Course
from planner.models import MyEvent


async def custom_save_my_event(text_data):
    try:
        name = text_data["name"]
        start_time = text_data["start_time"]
        student_id = text_data["student_id"]
        student = await database_sync_to_async(Student.objects.get)(id=student_id)
        my_event, _created = await database_sync_to_async(
            MyEvent.objects.update_or_create
        )(student=student, name=name, defaults={"start_time": start_time})
        return my_event
    except Exception as e:
        print(f"Error: {e}")


class EventConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if text_data_json["ssup"] == "creating":
            my_event = await custom_save_my_event(text_data_json)
            try:
                await self.send(
                    text_data=json.dumps(
                        {
                            "id": my_event.id,
                            "name": my_event.name,
                            "start_time": my_event.start_time,
                            "ssup": "created",
                        }
                    )
                )
            except Exception as e:
                print(f"Error when sending reply: {e}")

        elif text_data_json["ssup"] == "updating":
            my_event = await custom_save_my_event(text_data_json)
            try:
                await self.send(
                    text_data=json.dumps(
                        {
                            "id": my_event.id,
                            "name": my_event.name,
                            "start_time": my_event.start_time,
                            "ssup": "updated",
                        }
                    )
                )
            except Exception as e:
                print(f"Error when sending reply: {e}")

        elif text_data_json["ssup"] == "deleting":
            try:
                my_event = await database_sync_to_async(MyEvent.objects.get)(
                    id=text_data_json["id"]
                )
                await database_sync_to_async(my_event.delete)()
                await self.send(
                    text_data=json.dumps(
                        {
                            "name": text_data_json["name"],
                            "id": text_data_json["id"],
                            "ssup": "deleted",
                        }
                    )
                )
            except Exception as e:
                print(f"Error when sending reply: {e}")
