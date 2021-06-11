import socket

target_host = "127.0.0.1"
target_port = 9997

# Create the client, AF_INET is for IPv4 and SOCK_DGRAM is UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data, get http request
client.sendto(b"AAABBBCCC", (target_host, target_port))

data = client.recvfrom(4096)
print(data.decode())
client.close()
