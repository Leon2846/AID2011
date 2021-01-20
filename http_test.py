"""

"""

from socket import *

sock=socket()
sock.bind(("0.0.0.0",7878))
sock.listen(5)

connfd,addr=sock.accept()
print("Connect from",addr)

request=connfd.recv(1024)
print(request.decode())

# 组织响应
response="""HTTP/1.1 200 OK
Content-Type :text/html

hello world
"""

connfd.send(response.encode())

connfd.close()
sock.close()