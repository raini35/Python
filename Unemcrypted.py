import sys, socket, select

def server_socket(): 
	TO_HOST = ''
	AT_PORT = 13000
	LIST_OF_SOCKETS = []
	
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((TO_HOST, AT_PORT))
	server_socket.listen(10)
	LIST_OF_SOCKETS.append(server_socket)
	
	print "Chat room has begun." 
	
	while True: 
		ready_to_read,_,_ = select.select(LIST_OF_SOCKETS,[],[])
		
		for socket in ready_to_read: 
			if socket == server_socket: 
				client_socket, address = server_socket.accept()
				LIST_OF_SOCKETS.append(client_socket)
				print "Client " + address + " has been added to the chat room."
				
def client_socket(): 
	TO_HOST = "localhost" 
	AT_PORT = 13000
	BUF_SIZE = 1024
	
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.settimeout(1)
	
	client_socket.connect((TO_HOST, AT_PORT))
	
	print "You entered the chat room."
	print "What is your username?"
	username = sys.stdin.readline()
 	username = "[rfg40-" + username.rstrip('\n') + "]"
	sys.stdout.write(username); sys.stdout.flush()
	
	while True: 
		current_read_list = [sys.stdin, s]
		
		ready_to_read,_,_ = select.select(current_read_list, [], [])

		for socket in ready_to_read: 
			if socket == client_socket:
				message_from_other_client = socket.recv(BUF_SIZE)
				if not message_from_other_client: 
					print '\nDisconnected from server' 
					sys.exit()					
				else :
					sys.stdout.write(message_from_other_client) 
					sys.stdout.write(message_from_other_client); sys.stdout.flush()
			else:
				message_from_user = sys.stdin.readline()
				s.send(message_from_other_user)
				sys.stdout.write(username); sys.stdout.flush()
				
if __name__ == "__main__": 
	sys.exit(client_socket())