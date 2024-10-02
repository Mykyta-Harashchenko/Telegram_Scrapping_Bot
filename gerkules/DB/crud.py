from .models import User


async def save_user(data:dict):
    print("Start save")
    new_user = User(chat_id=data['chat_id'], first_name=data['first_name'], last_name=data['last_name'], language=data['language'])
    new_user.save()
    print("Save successfuly")


async def get_all_users():
    users = User.objects.all()
    return users