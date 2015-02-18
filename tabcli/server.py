import threading

from tabcli import rpc
from flask import Flask
app = Flask(__name__)

@app.route('/')
def show_tabs():
    rpc.send_message('{"command": "index"}')
    msg_raw = rpc.read_message()
    msg = json.loads(msg_raw.encode('utf-8'))
    return msg

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
