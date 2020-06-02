import socket
import datetime

with open('config', 'r') as f:
    dif = int(f.readline())
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 123))
print('Сервер запущен и готов к работе')
while True:
    client, address = server.recvfrom(123)
    if not client:
        break
    server.sendto(str(datetime.datetime.now() + datetime.timedelta(seconds=dif)).encode(), address)
server.close()
