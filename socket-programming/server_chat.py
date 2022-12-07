import socket

def server_program():
    host=socket.gethostname()
    port=5000
    
    server=socket.socket()
    server.bind((host, port))
    server.listen()
    
    conn, add = server.accept()
    print(conn)
    print("Connected to " + str(add))
    
    while True:
        data=conn.recv(1024).decode()
        
        if not data:
            break
        print(data)
        
        data=input("->")
        conn.send(data.encode())
    
    conn.close()
    server.close()

if __name__ =="__main__":
    server_program()
