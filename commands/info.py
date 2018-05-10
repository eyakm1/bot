import command_system


def info():
    message = ''
    for c in sorted(command_system.command_list, key=lambda x: x.priority_number):
        message += str(c.priority_number) + '. ' + c.keys[0] + ' - ' + c.description + '\n'
    return message, ''


info_command = command_system.Command()

info_command.keys = ['помощь', 'помоги', 'help']
info_command.description = 'Покажу список команд'
info_command.process = info
info_command.priority_number = 1