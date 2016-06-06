import socket     
from threading import Thread
from time import sleep

try:
  _ = raw_input
except NameError:
  raw_input = input

def ip():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(('192.168.1.1',80)) # this is the IP of our home router
  myIp = s.getsockname()[0]
  s.close()
  return myIp

def server_thread(arg):
  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serversocket.bind(arg)
  serversocket.listen(5) # become a server socket, maximum 5 connections
  connection, address = serversocket.accept()

  while True:    
    buf = connection.recv(64)
    if len(buf) > 0:
        print(buf)
        
def client_thread(arg):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(arg)

  while True:
    s.send(raw_input())


if __name__ == "__main__":
  server_ip = '192.168.1.10'
  client_ip = ip()
  server = Thread(target = server_thread, args = ((client_ip, 8089), ))
  client = Thread(target = client_thread, args = ((server_ip, 8089), ))
  server.start()
  client.start()
  server.join()
  client.join()
  