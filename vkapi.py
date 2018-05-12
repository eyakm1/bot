import vk
import random
import datetime
import settings

session = vk.AuthSession()
api = vk.API(session, v=5.74)
ban_session = vk.AuthSession(settings.app_id, settings.login, settings.passw, scope='manage')
ban_api = vk.API(ban_session, v=5.74)


def get_random_wall_picture(group_id):
    max_num = api.photos.get(owner_id=group_id, album_id='wall', count=0)['count']
    num = random.randint(1, max_num)
    photo = api.photos.get(owner_id=str(group_id), album_id='wall', count=1, offset=num)['items'][0]['id']
    attachment = 'photo' + str(group_id) + '_' + str(photo)
    return attachment


def get_random_quote(group_id, token):
    resp = api.wall.get(owner_id=group_id, count=1, access_token=token)
    max_num = resp['count']
    num = random.randint(1, max_num)
    quote = api.wall.get(owner_id=group_id, count=1, offset=num, access_token=token)['items'][0]
    quote_attach = quote['attachments'] if 'attachments' in quote else []
    message = quote['text']
    attachment = []
    if '#цитата_Доричи' in message:
        for attach in quote_attach:
            if attach['type'] in {'photo', 'video', 'audio', 'doc', 'wall', 'market'}:
                media_id = attach[attach['type']]['id']
                cur = str(attach['type']) + str(group_id) + '_' + str(media_id)
                attachment.append(cur)
        final_attach = ','.join(attachment)
        return message, final_attach


def ban_censorship(user, group):
    date_ban = int(datetime.datetime.now().timestamp()) + 3 * 60 * 60
    ban_api.groups.ban(group_id=group, owner_id=user, end_date=date_ban, reason=3, comment='За мат и двор стреляю в упор!',
                       comment_visible=1)


def send_message(user_id, token, message, attachment=""):
    api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment)
