import socket

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(),25000))
serversocket.listen()

connection, address = serversocket.accept()

print("connection has been established")

message="Hello client!"
connection.send(message.encode())

connection.close()
serversocket.close()
