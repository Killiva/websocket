#---------------------------------------------------------
# server.py
#---------------------------------------------------------

import socket
import threading

# Define some constants
HEADER = 64
PORT = 5050
# Get the IP address of the server machine
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
# The encoding to use when sending and receiving messages
FORMAT = 'utf-8'
# The message to send to the server to disconnect
DISCONNECT_MESSAGE = "!DISCONNECT"

# Create a new socket object and bind it to the address
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Function to handle a single client connection
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # Receive the length of the message
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            # Convert the message length to an integer and receive the actual message
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                # If the message is the DISCONNECT_MESSAGE, break out of the loop
                connected = False

            # Print the message and client address, and send an acknowledgment back to the client
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    # Close the connection when done
    conn.close()

# Function to start the server and listen for incoming connections
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # Accept a new client connection
        conn, addr  = server.accept()
        # Create a new thread to handle the connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # Print the number of active connections
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

# Print a message to indicate that the server is starting
print("[STARTING] server is starting..." )
# Call the start() function to start the server
start()
