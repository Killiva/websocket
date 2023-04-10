#---------------------------------------------------------
# client.py
#---------------------------------------------------------

import socket

# Define some constants
HEADER = 64
PORT = 5050
# The encoding to use when sending and receiving messages
FORMAT = 'utf-8'
# The message to send to the server to disconnect
DISCONNECT_MESSAGE = "!DISCONNECT"
# The IP address of the server to connect to
SERVER = "192.168.1.xxx"
ADDR = (SERVER, PORT)

# Create a new client socket and connect it to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Function to send a message to the server
def send(msg):
    # Encode the message into bytes using the specified encoding
    message = msg.encode(FORMAT)
    # Get the length of the message and encode it into bytes
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    # Pad the message length with spaces to the fixed length defined by HEADER
    send_length += b' ' * (HEADER - len(send_length))
    # Send the length and message to the server
    client.send(send_length)
    client.send(message)
    # Wait for an acknowledgment message from the server and print it
    print(client.recv(2048).decode(FORMAT))

# Send some test messages to the server
send("Hello World!")
# Wait for user input before sending the next message
input()
send("Hello Everyone!!!")
input()
send("Hello Mee!")

send(DISCONNECT_MESSAGE)