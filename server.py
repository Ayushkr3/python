import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('localhost', 7777))
s.listen(10)
conn,ca = s.accept()
print("conn by ",ca)
with conn:
    
    conn.recv(1024)
