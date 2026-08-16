import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("ВАШ_IP",10001))
socket.sendall("getter".encode("utf-8"))
print(socket.recv(1024).decode("utf-8"))
while True:
    data = socket.recv(1048576)
    name = socket.recv(1048576).decode("utf-8")
    if (data == b""):
        socket.close()
        break
    f = open(name,"wb")
    f.write(data)
    f.close() 
