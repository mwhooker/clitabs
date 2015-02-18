import json
import struct
import sys

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
        f.write('\n')

def read_message(stdin):
    # Read the message length (first 4 bytes).
    text_length_bytes = stdin.read(4)
    if len(text_length_bytes) == 0:
        sys.exit(0)
    # Unpack message length as 4 byte integer.
    text_length = struct.unpack('i', text_length_bytes)[0]
    # Read the text (JSON object) of the message.
    return stdin.read(text_length).decode('utf-8')


