import socket
host='localhost'
port=5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))
st=input("Type a message..")
while(str!='exit'):
    s.send(st.encode())
    data=s.recv(1024)
    data=data.decode()
    print("Arun :"+data)
    st=input("Type a message..:")

s.close()


