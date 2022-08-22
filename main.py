
import socket
con = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
con.connect(("8.8.8.8", 80))
result = con.getsockname()[0]
print(result)
con.close()


l = ['172.19.133.78', '127.0.0.1']

if result in l:
    print("Yes")


