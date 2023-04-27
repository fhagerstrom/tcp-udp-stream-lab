import socket
import time

startTime = time.time() # Measure execution time for fun

PACKET_SIZE = 1455 # A message packet is roughly 1455 bytes
UDP_IP = '192.168.1.75' # CHECK IP ON WHICH PC SHOULD ACT AS SERVER BEFORE RUNNING!
PORT_NUMBER = 5005
NUMBER_OF_MESSAGES = 1000
MESSAGE = b"x" * PACKET_SIZE
# MEESAGES_PER_SECOND = 50

print("IP address:", UDP_IP)
print ("Port number:", str(PORT_NUMBER), "\n")

sendingAddress = (UDP_IP, PORT_NUMBER) # Placeholder for IP / Port number
packetSeqNumber = 0
sentMessages = 0

# Create socket using IPv4 and UDP scheme
streamSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# While loop to send messages
while sentMessages < NUMBER_OF_MESSAGES:
    # Create message, convert sequence number to bytes
    seqNumBytes = packetSeqNumber.to_bytes(4, byteorder="big")
    
    msg = seqNumBytes + MESSAGE

    # Send message
    streamSocket.sendto(msg, sendingAddress)

    # Increment sequence number
    packetSeqNumber += 1

    # Send messages within a fixed time interval
    # time.sleep(0)

    sentMessages += 1 # Increment the amount of sent messages

    # print(msg) # Testprint the messages

# Send finishing characters to mark that the all messages are sent
streamSocket.sendto(b"\n####", sendingAddress)

# print("\n####") # Test print finishing characters.

# Close socket
streamSocket.close()

# Print execution time
print("--- Client execution time: %s seconds ---" % (time.time() - startTime))