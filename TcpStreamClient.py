import socket
import time

startTime = time.time() # Measure execution time for fun

PACKET_SIZE = 1455 # A message packet is roughly 1455 bytes
TCP_IP = '127.0.0.1' # CHECK IP ON WHICH PC SHOULD ACT AS SERVER BEFORE RUNNING!
PORT_NUMBER = 5005
NUMBER_OF_MESSAGES = 700
MESSAGE = b"x" * PACKET_SIZE
MESSAGES_PER_SECOND = 50

print("IP address:", TCP_IP)
print ("Port number:", str(PORT_NUMBER), "\n")

sendingAddress = (TCP_IP, PORT_NUMBER) # Placeholder for IP / Port number
packetSeqNumber = 0
sentMessages = 0

# Create socket using IPv4 and TCP scheme
streamSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
streamSocket.connect(sendingAddress)

# While loop to send messages
while sentMessages < NUMBER_OF_MESSAGES:
    # Create message, convert sequence number to bytes
    seqNumBytes = packetSeqNumber.to_bytes(2, byteorder="big")
    
    msg = seqNumBytes + MESSAGE

    print("Sending message...")
    # Send message
    streamSocket.send(msg)

    # Increment sequence number
    packetSeqNumber += 1

    # print("Sleep timer...")
    # Send messages within a fixed time interval
    time.sleep(1 / MESSAGES_PER_SECOND)

    sentMessages += 1 # Increment the amount of sent messages

    # print("Receiving from server...")
    data = streamSocket.recv(1024).decode()  # Receive response from server       
    print(data)  # Show in terminal

    # print(msg) # Testprint the messages locally

# Send finishing characters to mark that the all messages are sent
streamSocket.send(b"\n####")

# print("\n####") # Test print finishing characters.

# Close socket
streamSocket.close()

# Print execution time
print("--- Client execution time: %s seconds ---" % (time.time() - startTime))