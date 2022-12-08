import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

serverAddressPort   = ("127.0.0.1", 6002)

while True:
    message = input("Enter you message -->  ")

    s.sendto(message.encode(),serverAddressPort)
    if message =="END":
        break

received = s.recvfrom(1024)
message = received[0].decode()

print(message)
