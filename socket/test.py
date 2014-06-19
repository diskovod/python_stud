import socket

sock = socket.socket()
sock.bind(('localhost', 8080))
sock.listen(5)
client, adress = sock.accept()

print "Incoming:", adress
print client.recv(1024)

client.send('HTTP/1.0 200 OK\r\n')
client.send("Content-Type: text/html\r\n\r\n")
client.send('<html><body><h1>Hello World1111</body></html>')
client.close()

print "Answering ..."
print "Finished."

sock.close()
