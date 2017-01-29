import sys
import socket
import select

def chat_client(): 
	TO_HOST = "localhost" 
	AT_PORT = 13003
	BUF_SIZE = 1024
	
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.settimeout(2)
	
	client_socket.connect((TO_HOST, AT_PORT))
	
	print "You entered the chat room."
	print "What is your username?"
	username = sys.stdin.readline()
 	username = "[rfg40-" + username.rstrip('\n') + "]"
	sys.stdout.write(username); sys.stdout.flush()
	
	while True: 
		read_list = [sys.stdin, client_socket] 
		
		ready_to_read,_,_ = select.select(read_list, [], [])
		
		for current_socket in ready_to_read:
			if current_socket == client_socket: 
				message_from_current_socket = current_socket.recv(BUF_SIZE)
				if not message_from_current_socket:
					print '\nDisconnected from server' 
					sys.exit()	
				else: 
					sys.stdout.write(message_from_current_socket)
					sys.stdout.write(username); sys.stdout.flush()
			else: 
				message_from_user = sys.stdin.readline()
				client_socket.send(message_from_user) 
				sys.stdout.write(username); sys.stdout.flush()

if __name__ == "__main__":
	sys.exit(chat_client())