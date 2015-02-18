import StringIO
import json
import uuid
import sys
import threading

from tabcli import rpc
from flask import Flask


stdin = sys.stdin
sys.stdin = StringIO.StringIO()

app = Flask(__name__)
app.debug = True

def send_message(command, params=None):
    if params is None:
        params = {}
    payload = dict(params)
    payload['command'] = command
    payload['_id'] = str(uuid.uuid4())
    rpc.send_message(json.dumps(payload))

def read_message():
    msg_raw = rpc.read_message(stdin).encode('utf-8')
    msg = json.loads(msg_raw)
    return msg

@app.route('/')
def show_tabs():
    # rpc.log_message("reading stdin: %s" % sys.stdin.read())
    send_message('index')
    msg = read_message()
    rpc.log_message("received: " + msg['_id'])
    return str(msg)

def app_main():
    pass

def rpc_main():
    app.run(port=5427)

def main():
    # app_thread = threading.Thread(target=app_main)
    # app_thread.start()
    rpc_main()

if __name__ == '__main__':
    main()
