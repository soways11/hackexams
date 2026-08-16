import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0",10001))
while True:
    print("new connection")
    server.listen(2)
    socket_sender = 0
    ip_sender = 0
    socket_getter = 0
    ip_getter = 0
    got_sender = 0
    got_getter = 0
    while True:
        cur_socket, cur_ip = server.accept()
        name = cur_socket.recv(1024).decode("utf-8")
        if (name == "sender"):
            socket_sender = cur_socket
            ip_sender = cur_ip
            got_sender = 1
            print("Sender connected")
        elif (name == "getter"):
            socket_getter = cur_socket
            ip_getter = cur_ip
            got_getter = 1
            print("Getter connected")
        if (got_sender == 1 and got_getter == 1):
            break
    print("Ready for a transfer")
    socket_sender.sendall("Ready for a transfer".encode("utf-8"))
    socket_getter.sendall("Ready for a transfer".encode("utf-8"))
    while True:
        try:
            data = socket_sender.recv(1048576)
        except:
            socket_sender.close()
            socket_getter.close()
            break
        try:
            socket_getter.sendall(data)
        except: 
            socket_sender.close()
            socket_getter.close()
            break
        if data == b"":
            socket_sender.close()
            socket_getter.close()
            break
