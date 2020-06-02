import socket
import datetime
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'TIME', ('127.0.0.1', 123))
print(f'Реальное время: {str(datetime.datetime.now())}')
print(f'Время от сервера: {s.recvfrom(1024)[0].decode()}')
s.close()
