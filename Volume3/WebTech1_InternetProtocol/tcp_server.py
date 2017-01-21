import socket

# Define the parameters of the tcp connection
ip = '127.0.0.1' # The local machine
port = 33498 # Arbitrary port number
size = 2048  # Normally 1024, but we want fast response

# Create a new socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind it to our desired address and port
s.bind((ip, port))
# Start listening for requests
s.listen(1)

# Accept a request when one comes
conn, addr = s.accept()
print "Accepting connection from: ", addr
while True:
    # Read 20 bytes from the incoming connection
    data = conn.recv(size)
    # If we have note received any data, we terminate the connection
    if not data:
        break
    # Otherwise we send back the data we received from the client
    print "Echoing data: ", data
    conn.send(data)  # echo
conn.close()
