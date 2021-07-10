import socket
def urlsearch():
    try:
        result = socket.getaddrinfo("howard1115.synology.me", None)
        result = result[0][4][0]
        return result
    except:
        try:
            result = socket.getaddrinfo("howard115.synology.me", None)
            result = result[0][4][0]
            return result
        except:
            print("域名解析失败")
print(urlsearch())