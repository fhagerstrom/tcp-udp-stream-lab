import socket
import time

startTime = time.time() # Measure execution time for fun

PACKET_SIZE = 1455 # A message packet is roughly 1455 bytes
IP_ADDRESS = '192.168.1.75' # CHECK IP ON WHICH PC SHOULD ACT AS SERVER BEFORE RUNNING!
PORT_NUMBER = 5005
NUMBER_OF_MESSAGES = 3000
MESSAGE = b"x" * PACKET_SIZE
# MEESAGES_PER_SECOND = 50

print("IP address:", IP_ADDRESS)
print ("Port number:", str(PORT_NUMBER), "\n")

sendingAddress = (IP_ADDRESS, PORT_NUMBER) # Placeholder for IP / Port number
packetSeqNumber = 0
sentMessages = 0

# Create socket using IPv4 and UDP scheme
datagramSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# While loop to send messages
while sentMessages < NUMBER_OF_MESSAGES:
    # Create message, convert sequence number to bytes
    seqNumBytes = packetSeqNumber.to_bytes(2, byteorder="big")
    
    msg = seqNumBytes + MESSAGE

    # Send message
    datagramSocket.sendto(msg, sendingAddress)

    # Increment sequence number
    packetSeqNumber += 1

    # Send messages within a fixed time interval, specified by SLEEP_TIMER
    time.sleep(0)

    sentMessages += 1 # Increment the amount of sent messages

    # print(msg) # Testprint the messages

# Send finishing characters to mark that the all messages are sent
datagramSocket.sendto(b"\n####", sendingAddress)

# print("\n####") # Test print finishing characters.

# Close socket
datagramSocket.close()

# Print execution time
print("--- Client execution time: %s seconds ---" % (time.time() - startTime))