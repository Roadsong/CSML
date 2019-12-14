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
        print(CMD_LINE)
        clientSock.sendto(CMD_LINE.encode(), (MANAGEMENT_ADDR, MANAGEMENT_PORT))


    def save(self):
        # Save a request
        # For simplicity, not support now
        pass

    def enumerate(self):
        # List all saved request
        # For simplicity, not support now
        pass


CMD_LINE = "cat /proc/self/cgroup | grep \"cpu:/\" | sed 's/\([0-9]\):cpu:\/docker\///g' > /id.log"
os.system(CMD_LINE)
with open("/id.log", "r") as f:
    for line in f:
        # Only one line
        container_id = line[:-1]
        print(container_id)

USER_ADDR = container_id[0:12]
USER_PORT = 8899
print(USER_ADDR)
print(USER_PORT)
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((USER_ADDR, USER_PORT))

def main():

    # (self, app, container_id, simple_request = True, upload_file = None, operation = None):
    my_request = ClientRequest("opencv", container_id, True, None, None)
    my_request.send()
    buf = serverSock.recv(1024)
    print(buf.decode('utf-8'))


if __name__ == "__main__":
    main()