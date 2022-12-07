import socket

def client_program():
    host=socket.gethostname()
    port=5000

    client=socket.socket()
    client.connect((host,port))

    msg=input("->")

    while msg.lower().strip() != "bye":
        client.send(msg.encode())
        data=client.recv(1024).decode()
    
        print("Received from the server: "+str(data))
    
        msg=input("->")
    
    client.close()

if __name__ =="__main__":
    client_program()
