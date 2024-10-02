from mongoengine import Document, IntField, StringField, ReferenceField,DateTimeField, BooleanField
from datetime import datetime
from .connect import connect, db_name


class User(Document):
    meta = {'db_alias': db_name}
    chat_id = IntField(unique=True)
    first_name = StringField()
    last_name = StringField(default='')
    language = StringField()
    created_at = DateTimeField(default=datetime.now)
    is_active = BooleanField(default=True)