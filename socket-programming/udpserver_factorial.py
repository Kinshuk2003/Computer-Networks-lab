import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

host = '127.0.0.1'
port = 6002

s.bind((host,port))

addrpair = s.recvfrom(1024)
count +=1
message = addrpair[0].decode()
address = addrpair[1]
print(message)
    
n=int(message)
p=1
while n>1:
    p = p*n
    n -=1
message = str(p).encode()

s.sendto(message,address)
