import command_system
import vkapi
import settings


def quote():
    msg, attach = vkapi.get_random_quote(-159191596, settings.service_token)


quote_command = command_system.Command()

quote_command.keys = ['цитатка', "цитата", "цитатеночка"]  # Ну а какие еще команды???
quote_command.description = 'Пришлю картинку с котиком'
quote_command.process = quote
