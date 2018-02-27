#import socket module 
from socket import *                                   
serverSocket = socket(AF_INET, SOCK_STREAM) 
#Prepare a sever socket 
#Fill in start 
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind((gethostname(), 8000))
serverSocket.listen(1)
#Fill in end 
while True: 
    #Establish the connection 
    print 'Ready to serve...' 
    connectionSocket, addr = serverSocket.accept() 
    try: 
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]                  
        f = open(filename[1:])                         
        outputdata = f.read()
        #Send one HTTP header line into socket
        #Fill in start 
        connectionSocket.send('HTTP/1.1 200 OK\n\n')
        # connectionSocket.send('Connection: close\r\n')
        #Fill in end                 
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):       
            connectionSocket.send(outputdata[i])   
        connectionSocket.close()
    except IOError: 
        #Send response message for file not found 
#Fill in start
        connectionSocket.send('HTTP/1.1 404 Not Found\n\n')
        #Fill in end 
#Close client socket
        #Fill in start 
        connectionSocket.send('404 Not Found\n')
        connectionSocket.close() 
        #Fill in end        
serverSocket.close()                                     