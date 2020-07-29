"""
The UDPserver receives requests from a UDPclient, 
converts the messages to uppercase and return them.
"""
from socket import *

# specifying the port to which the socket will connect
server_port = 12000

# creating a server socket
# AF_INET - For IPv4, SOCK_DGRAM - For UDP protocol
server_socket = socket(AF_INET, SOCK_DGRAM)

# attaching the server socket to the server_port
# to moniter incoming requests
server_socket.bind(('', server_port))

while 1:
	# waiting for a packet to arrive
	message, client_address = server_socket.recvfrom(2048)
	# converting the message to uppercase
	reply = message.upper()
	# replying the converted text back to the client
	server_socket.sendto(reply, (client_address))

	print('request: ', message.decode('utf-8'))
	print('client_address: ', client_address)
	print('reply: ', reply.decode('utf-8'))