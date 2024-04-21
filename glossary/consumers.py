# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from notes.models import Course
from glossary.models import Term


async def custom_save_term_inline(text_data):
    try:
        text_data_json = json.loads(text_data)
        term = text_data_json["term"]
        definition = text_data_json["definition"]
        cert_id = text_data_json["course_id"]
        course = await database_sync_to_async(Course.objects.get)(
            id=cert_id
        )
        term = Term(course=course, name=term, definition=definition)
        await database_sync_to_async(term.save)()
        return term
    except Exception as e:
        print(f"Error: {e}")


class TermInlineConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        term = await custom_save_term_inline(text_data)

        try:
            await self.sendTermInline(
                {
                    "term": term.name,
                    "definition": term.definition,
                }
            )
        except Exception as e:
            print(e)

    async def sendTermInline(self, event):
        try:
            term = event["term"]
            definition = event["definition"]
            text_data = json.dumps(
                {
                    "term": term,
                    "definition": definition,
                }
            )

            await self.send(text_data=text_data)
        except Exception as e:
            print(e)
