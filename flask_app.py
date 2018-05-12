# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, json
from settings import *
import sys
import messageHandler

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Dorichenishi!'


@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)
    print(data, file=sys.stderr)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], token)
        return 'ok'
