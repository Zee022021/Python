# first of all we are importing the socket library
import socket
# next create a socket object
s = socket.socket()
print('Socket successfully created')
# reserve a port number
port = 12345
# bind to the port
s.bind(('', port))
print('socket binded to %s' %(port))
# put the socket into listening mode
s.listen(5)
print('socket is now listening')
# a forever loop until we exit
# or an error occurs 
while True:
    # Establish connection with client
    c, addr = s.accept()
    print('Got connection', addr)
    # Close the connection with the client
    c.close()
    # Breaking once connection closed
    break