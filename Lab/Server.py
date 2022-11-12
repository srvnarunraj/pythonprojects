import socket

host = 'localhost'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
print("Whatsapp is live,Waiting for ur friend")
s.listen(1)
c, address = s.accept()
print("friend is online")
print("Friend:", str(address))
while True:
    data = c.recv(1024)
    if not data:
        break
    print("Friend:" + data.decode())
    data1 = input('Type a message...')
    c.send(("Arun :" + data1).encode())
s.close
