"""
The TCPclient sends a request to the server to convert a sentence to uppercase.
The server accepts the request, converts and sends back the converted text.
"""
from socket import *

# specifying the ip address or the name of the server
server_name = '127.0.0.1'
# specifying a random port number
server_port = 12000

# creating a client socket
# AF_INET - For IPv4, SOCK_STREAM - For TCP Protocol
# port is assigned to client_socket by the OS automatically
client_socket = socket(AF_INET, SOCK_STREAM)

# initiates TCP connection after a three-way handshake
client_socket.connect((server_name, server_port))

# creates a message to send to the server
message = input('Enter sentence to be converted to uppercase:')

# sending the message to the server
client_socket.send(message.encode())

# waiting for the reply from the server
# 2048 is the buffer size
reply = client_socket.recv(2048)

# displaying the reply
print('Reply From Server: ', reply.decode('utf-8'))

# closing the socket connection
client_socket.close()