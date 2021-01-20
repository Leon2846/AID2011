"""

"""
from socket import *

def handle(connfd):
    request=connfd.recv(1024).decode()
    if not request:
        return
    response="HTTP/1.1 200 OK\r\n"
    response+="Content-Type:text/html\r\n"
    response+="\r\n"
    with open("my.html") as f:
        response+=f.read()
    connfd.send(response.encode())

def main():
    sock=socket()
    sock.bind(("0.0.0.0",8000))
    sock.listen(5)

    connfd,addr=sock.accept()
    print("Connect from",addr)
    handle(connfd)
    connfd.close()

if __name__ == '__main__':
    main()