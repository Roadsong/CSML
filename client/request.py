import os
import sys
import socket

# Mac: server
# Pi: client

MANAGEMENT_PORT = 9983
MANAGEMENT_ADDR = "csml-management-server" # For local testing, maybe we can have a real test with an ubuntu?
apps = ("opencv", "dynet", "dlib")

class ClientRequest():
    def __init__(self, app, container_id, simple_request = True, result_file = None, upload_file = None, operation = None):
        super(ClientRequest, self).__init__()
        self.app = app # type:str
        self.container_id = container_id # type:str
        self.simple_request = simple_request # type:bool
        self.result_file = result_file # type:str (location)

        # For simplicity, currently only support simple request unit tests
        self.upload_file = upload_file # type:str (location)
        self.operation = operation # type:str

    def send(self):
        # Create an client socket
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Send request to server (mangement)
        # For simplicity, currently only support simple request unit test
        CMD_LINE = "app:" + self.app + ":id:" + self.container_id + ":request_type:" + str(self.simple_request)
        clientSock.sendto(CMD_LINE, (MANAGEMENT_ADDR, MANAGEMENT_PORT))

        # Waiting for response
        # If result_file is set, append the result, otherwise printing on screen


    def save(self):
        # Save a request
        # For simplicity, not support now
        pass

    def enumerate(self):
        # List all saved request
        # For simplicity, not support now
        pass


