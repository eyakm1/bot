import vkapi
import os
import importlib
from command_system import command_list


def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1
    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,  # deletion
                d[(i, j - 1)] + 1,  # insertion
                d[(i - 1, j - 1)] + cost,  # substitution
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition
    return d[lenstr1 - 1, lenstr2 - 1]


def load_modules():
    files = os.listdir("mysite/commands")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])


def get_answer(body):
    message = ""
    attachment = ''
    distance = len(body)
    command = None
    key = ''
    for c in command_list:
        for k in c.keys:
            d = damerau_levenshtein_distance(body, k)
            if d < distance:
                distance = d
                command = c
                key = k
                if distance == 0:
                    message, attachment = c.process()
                    return message, attachment
    if distance < len(body) * 0.4:
        message, attachment = command.process()
        message = 'Я понял ваш запрос как "%s"\n\n' % key + message
    if message:
        return message, attachment


def create_answer(data, token):
    load_modules()
    user_id = data['user_id']
    message, attachment = get_answer(data['body'].lower())
    with open(r'mysite/bad_words.txt', 'r', encoding='utf-8') as fin:
        body_words = list(map(lambda x: x.strip(), data['body'].lower().split()))
        if any(word in fin.read().split('\n') for word in body_words):
            vkapi.ban_censorship(group=159191596, user=user_id)
            message = 'Вот только ненадо тут этих слов! 😡 За это тебя покарал Бог Доричёнышей на 3 часа!!! 😡😡😡 Только потом подписаться обратно не забудь 😋'
    vkapi.send_message(user_id, token, message, attachment)
