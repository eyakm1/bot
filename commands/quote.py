import command_system
import vkapi


def quote():
    msg, attach = vkapi.get_random_quote()