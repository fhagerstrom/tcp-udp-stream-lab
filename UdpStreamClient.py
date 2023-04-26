import socket
import time

ip = 'hostname' # CHECK IP ON PC WHO SHOULD ACT AS CLIENT BEFORE RUNNING
portNum = 9999

print("IP address of client is:", ip)
print ("On port number:", str(portNum), "\n")
listeningAddress = (ip, portNum)

# Create datagram socket using IPv4 and UDP scheme
datagramSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open text file that will be sent to server as packets.
with open('streamMessage.txt', 'r') as file: 
    msg = file.read()
    file.close()

print(msg)