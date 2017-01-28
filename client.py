import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('',12027))
print "Connected to server"

print "Hello Client"

while True: 
	message = raw_input(">>>")
	s.send(message)
	
	
s.close()