import argparse 
import socket 
import select
import sys 

parser = argparse.ArgumentParser()
parser.add_argument("--s", dest="server", help="Turn on server", action='store_true')
parser.add_argument("--c", dest="client", help="Turn on client")
args = parser.parse_args()


if args.server == True:
	name = raw_input("What is your username?")
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(('',10010))
	s.listen(5)
	clientsocket, address = s.accept()
	client_name = clientsocket.recv(1024)
	print "Got connection from ",
	print address
	
	while True:
		data = clientsocket.recv(1024)
		print "[" + client_name + "]",
		print data
		
	print "Hello Server"
	s.close()
	
if args.client != None:
	name = raw_input("What is your username?")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('',10010))
	s.send(name)
	print "Connected to server as " + name
	
	print "Hello Client"
	
	while True: 
		message = raw_input("[" + name  + "]")
		s.send(message)
		
	s.close()