import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(("ВАШ_IP",10001))
socket.sendall("sender".encode("utf-8"))
print(socket.recv(1024).decode("utf-8"))
while True:
    adress = input()
    try:
        f = open(adress, "rb")
        data = f.read()
        f.close()
    except:
        print("Wrong adress")
        continue
    try:
        socket.sendall(data)
        socket.sendall(adress[max(adress.rfind("\\"), adress.rfind("/"))+1:].encode("utf-8"))
    except: 
        socket.close()
        break
