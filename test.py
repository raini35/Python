import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect( ("HostB", 9999) ) 
s.send('hello world')
s.close