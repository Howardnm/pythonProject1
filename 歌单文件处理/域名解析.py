import socket
result = socket.getaddrinfo("howard115.synology.me", None)
print(result[0][4][0])