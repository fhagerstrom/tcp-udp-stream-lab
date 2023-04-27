import socket
import time
import select
import sys

startTime = time.time() # Measure execution time.

# Define fixed variables such as packet size, IP, port number, number of messages, etc.
# A packet size is roughly 1455 bytes
PACKET_SIZE = 1475 # 2 bytes buffer for sequence number, 1455 for message, 16 for UDP header
TCP_IP = '127.0.0.1' # CHECK IP ON WHICH PC SHOULD ACT AS SERVER BEFORE RUNNING
PORT_NUMBER = 5010
NUMBER_OF_MESSAGES = 1000

print("IP address:", TCP_IP)
print ("Port number:", str(PORT_NUMBER), "\n")

listeningAddress = (TCP_IP, PORT_NUMBER)

# Create server socket using IPv4 and TCP scheme
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to IP address and port number
serverSocket.bind(listeningAddress)

# Incoming connections.
serverSocket.listen()

print("Server ready to receive!\n")

# Create variable to keep track of expected packet sequence number
expectedSeqNumber = 0

# While condition for client messages
recievedMessages = 0

# Open a file where we log if the sequence number was higher / lower than expected
expectedSequenceFile = open("StreamLogs/StreamSeqLog.txt", "w")

# Recieve the messages from the client
while recievedMessages < NUMBER_OF_MESSAGES:
    # Set timeout for 5 seconds
    ready = select.select([serverSocket], [], [], 5)

    if ready[0]:
        # Wait for incoming messages.
        clientSocket, address = serverSocket.accept()

        # Recieve messages and address from client
        msg = serverSocket.recv(PACKET_SIZE)

        # Extract packet sequence number of the message to keep track of incoming packets
        packetSeqNumber = int.from_bytes(msg[:2], byteorder="big")

        # Check expected sequence number
        if packetSeqNumber != expectedSeqNumber:
            checkMsg = "Warning: Received message with sequence number %d, expected %d\n" % (packetSeqNumber, expectedSeqNumber)
            expectedSequenceFile.write(checkMsg)

        msgText = msg[2:].decode() # Slice the message from client since the sequence number comes first

        # Print where the message comes from, which packet sequence number it is, and the message itself
        print("Received message from %s\nSequence number: %d\nMessage: \%s\"" % (address, packetSeqNumber, msgText))

        expectedSeqNumber += 1 # Increment sequence number after receieved message
        expectedSequenceFile.write(str(expectedSeqNumber) + "\n")

        recievedMessages += 1

    else:
        print("Timeout reached. Exiting...")
        sys.exit()

# Close log file and socket.
expectedSequenceFile.close()
serverSocket.close()

# Print execution time
print("--- Server execution time: %s seconds ---" % (time.time() - startTime))