import os
import sys
import socket

# Mac: server
# Pi: client
# For local testing, maybe we can have a real test with an ubuntu?

MANAGEMENT_PORT = 9983
MANAGEMENT_ADDR = "csml-management" 
apps = {"opencv":9980, "dynet":9981, "dlib":9982}

class ClientRequest():
    def __init__(self, app, container_id, simple_request = True, upload_file = None, operation = None):
        super(ClientRequest, self).__init__()
        self.app = app # type:str
        self.container_id = container_id # type:str
        self.simple_request = simple_request # type:bool

        # For simplicity, currently only support simple request unit tests
        self.upload_file = upload_file # type:str (location)
        self.operation = operation # type:str

    def send(self):
        # Create an client socket
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        if self.simple_request:
            simple_request = 'Y'
        else:
            # Not support now
            simple_request = 'N'

        # Send request to server (mangement)
        # For simplicity, currently only support simple request unit test
        CMD_LINE = self.app + ":" + str(self.container_id) + ":" + simple_request 
        clientSock.sendto(CMD_LINE.encode(), (MANAGEMENT_ADDR, MANAGEMENT_PORT))

        # Waiting for response
        data, server_addr = clientSock.recvfrom(1024)


    def save(self):
        # Save a request
        # For simplicity, not support now
        pass

    def enumerate(self):
        # List all saved request
        # For simplicity, not support now
        pass


