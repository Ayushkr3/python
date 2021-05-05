import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1', 7777))
s.listen(10)
while True:
    
    conn,ca = s.accept()
    print("conn by ",conn)
    conn.recv(1024)
