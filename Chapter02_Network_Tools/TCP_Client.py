import socket

target_host = "192.168.56.102"
target_port = 9998

# Create the client, AF_INET is for IPv4 and SOCK_STREAM is tcp
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

# Send some data, get http request
client.send(b"Hello Kali, This is Mac")

resp = client.recv(4096)
print(resp.decode())
client.close()
