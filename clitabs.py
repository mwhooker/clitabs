#!/usr/bin/env python


import sys
import struct

def send_message(message):
    log_message("sending: %s" % message)
    # Write message size.
    sys.stdout.write(struct.pack('I', len(message)))
    # Write the message itself.
    sys.stdout.write(message)
    sys.stdout.flush()

def log_message(message):
    with open("/Users/mwhooker/dev/tabcli/log", "a+") as f:
        f.write(message)


send_message('{"text": "starting"}')


#for line in sys.stdin:
#    send_message("got ur message.")
#    log_message("input: %s" % line)
# if __name__ == "__main__":
while True:
    # Read the message length (first 4 bytes).
    text_length_bytes = sys.stdin.read(4)
    if len(text_length_bytes) == 0:
        sys.exit(0)
    # Unpack message length as 4 byte integer.
    text_length = struct.unpack('i', text_length_bytes)[0]
    # Read the text (JSON object) of the message.
    text = sys.stdin.read(text_length).decode('utf-8')
    # In headless mode just send an echo message back.
    send_message('{"echo": %s}' % text)
