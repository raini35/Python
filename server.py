import socket, select 

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.bind(('', 12027))
listen_socket.listen(10)
client_sockets = []


while True: 
	message = raw_input(">>> ")
	
	read_list = [listen_socket] + client_sockets
	(ready_read, _,_) = select.select(read_list, [], [], 0)
	
	if len(ready_read) != 0 :
		for sock in ready_read: 
			if sock is listen_socket:
				new_conn, addr = sock.accept()
				client_sockets.append(new_conn)
			else: 
				sock.send("bitch")
				data = sock.recv(1024)
				if data != "": 
					print data
				else:
					client_sockets.remove(sock)
					sock.close()
				
