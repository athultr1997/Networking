"""
The UDPserver receives requests from a UDPclient, 
converts the messages to uppercase and return them.
"""
from socket import *

# specifying the port to which the socket will connect
server_port = 12000

# creating a server socket
# AF_INET - For IPv4, SOCK_STREAM - For TCP protocol
server_socket = socket(AF_INET, SOCK_STREAM)

# server_socket is the welcoming socket
server_socket.bind(('', server_port))

# waiting for client requests
# 1 is the maximum no:of queued connections
server_socket.listen(1)

while 1:
	# handshaking happens between the connection_socket and the client_socket
	connection_socket, addr = server_socket.accept()
	# waits for a packet to arrive
	message = connection_socket.recv(2048)
	# converting the message to uppercase
	reply = message.upper()
	# replying the converted text back to the client
	connection_socket.send(reply)
	connection_socket.close()

	print('request: ', message.decode('utf-8'))	
	print('reply: ', reply.decode('utf-8'))




