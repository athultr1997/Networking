import socket

def find_file_name(request):
	request = request.decode('utf-8')
	request = request.split()
	return request[1][1:]

server_port = 12000

try:
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print('server socket created successfully')
except socket.error:
	print('server socket connection failed:', socket.error)

server_socket.bind(('', server_port))
server_socket.listen(1)

while 1:	
	connection_socket, addr = server_socket.accept()	
	message = connection_socket.recv(2048)
	
	file_name = find_file_name(message)

	try:
		with open(file_name) as file:
			data = file.read()	
			reply = 'HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: {}\n\n{}' \
					.format(len(data.encode()), data).encode()
	except IOError:
		data = 'Not Found'
		reply = 'HTTP/1.1 404 Not Found\nConnection: close\nContent-Type: text/html\nContent-Length: {}\n\n{}' \
		        .format(len(data.encode()), data).encode()

	connection_socket.send(reply)	
	connection_socket.close()	

	print('request: \n\n', message)	
	print('reply: \n\n\n', reply.decode('utf-8'))
	print('-'*50)