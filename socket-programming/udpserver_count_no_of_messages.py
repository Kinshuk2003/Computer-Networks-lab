import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

host = '127.0.0.1'
port = 6002

s.bind((host,port))
count=0
while True:
    addrpair = s.recvfrom(1024)
    count +=1
    message = addrpair[0].decode()
    address = addrpair[1]
    if message =="END":
        break

message = str(count).encode()

s.sendto(message,address)
