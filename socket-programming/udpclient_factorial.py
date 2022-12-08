import socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

serverAddressPort   = ("127.0.0.1", 6002)

message = input("Enter The Number -->  ")

s.sendto(message.encode(),serverAddressPort)

received = s.recvfrom(1024)
message = received[0].decode()

print("Factorial of the Number: " + str(message))
