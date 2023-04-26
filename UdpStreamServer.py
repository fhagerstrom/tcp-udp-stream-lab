import socket
import time
import numpy

BUFFER_SIZE = 4096

# Define IP address of server and port number
ip = '193.11.184.62' # CHECK IP ON PC WHO SHOULD ACT AS SERVER BEFORE RUNNING
portNum = 9999

print("IP address of server is:", ip)
print ("On port number:", str(portNum), "\n")
listeningAddress = (ip, portNum)

# Create datagram socket using IPv4 and UDP scheme
datagramSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
datagramSocket.bind(listeningAddress)

establishedConnection = True

while(establishedConnection):
    msg, clientAddress = datagramSocket.recvfrom(BUFFER_SIZE)
    print("Got connection from:", clientAddress, "\n")

    
