import socket
from time import sleep

TCP_IP = '0.0.0.0'
PORT = 55555
BUFFER_SIZE = 2048
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, PORT))
print(s.recv(BUFFER_SIZE))

def send_command(command):
  s.send(command)
  data = s.recv(BUFFER_SIZE)

  print (data)

send_command('where robot')
send_command('speed 9 9')
sleep(2)
send_command('speed 0 0')
sleep(2)
send_command('speed -9 -5')
sleep(2)
send_command('speed -2 10')
sleep(2)
send_command('speed 0 0')
send_command('where robot')
s.close()
