import command_system


def bye():
   message = 'Пока! И да прибудет с тобой СерСан!'
   return message, ''

bye_command = command_system.Command()

bye_command.keys = ['пока', 'bye', 'досвидос', 'досвидания', 'прощай', 'бай']
bye_command.description = 'Попрощаюсь с тобой'
bye_command.process = bye
bye_command.priority_number = 5
