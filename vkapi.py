import vk
import random

session = vk.Session()
api = vk.API(session, v=5.0)


def get_random_wall_picture(group_id):
    max_num = api.photos.get(owner_id=group_id, album_id='wall', count=0)['count']
    num = random.randint(1, max_num)
    photo = api.photos.get(owner_id=str(group_id), album_id='wall', count=1, offset=num)['items'][0]['id']
    attachment = 'photo' + str(group_id) + '_' + str(photo)
    return attachment


def get_random_quote(group_id):
    resp = api.wall.get(owner_id=group_id, count=0)
    max_num = resp['count']
    num = random.randint(1, max_num)
    quote = api.wall.get(owner_id=group_id, count=1, offset=num)['items'][0]
    quote_attach = quote['attachments']
    message = quote['text']
    attachment = []
    for attach in quote_attach:
        if attach['type'] in {'photo', 'video', 'audio', 'doc', 'wall', 'market'}:
            media_id = attach[attach['type']]['id']
            cur = str(attach['type']) + str(group_id) + '_' + str(media_id)
            attachment.append(cur)
    return message, ','.join(attachment)


def send_message(user_id, token, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)