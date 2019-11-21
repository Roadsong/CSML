import os
import sys
import socket
import request_queue
from config import *

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((MANAGEMENT_ADDR, MANAGEMENT_PORT))


# Check the target app is vacant or not
def is_vacant(app):
    # Check the load of an app docker
    # How to check? Cannot using cpu indicator because resources are shared!
    return True


# Send request to target app
# SOURCE_ADDR for future use
def send_request(app, CMD_LINE, SOURCE_ADDR):
    APP_ADDR = "csml-" + app # type:str
    APP_PORT = apps[app] # type:int

    # Create an socket and forward the message to target app
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSock.sendto(CMD_LINE + "|" + SOURCE_ADDR, (APP_ADDR, APP_PORT))
    clientSock.close()


# Send back useful information to user
def send_info(info, SOURCE_ADDR):
    # Discard and send back the info
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSock.sendto(info, SOURCE_ADDR)
    clientSock.close()


def main():
    cv_q = request_queue.ClientRequestQueue("opencv")
    print("Initiate Opencv Queue.")
    print(cv_q.maxsize)

    dynet_q = request_queue.ClientRequestQueue("dynet", 100)
    print("Initiate DyNet Queue.")
    print(dynet_q.maxsize)
    
    dlib_q = request_queue.ClientRequestQueue("dlib", 100)
    print("Initiate Dlib Queue.")
    print(dlib_q.maxsize)

    while True:

        print("Waiting...")
        CMD_LINE, SOURCE_ADDR = serverSock.recvfrom(1024)
        print("Received a request.")

        # Format
        # app:container_id:simple_request
        app = CMD_LINE.split(":")[0] # type:str

        if app == "opencv":
            if cv_q.qsize() < cv_q.maxsize:
                cv_q.put((CMD_LINE, SOURCE_ADDR))
                info = "Request now in opencv queue."
            else:
                info = "Opencv queue full now."
        elif app == "dynet":
            if dynet_q.qsize() < dynet_q.maxsize:
                dynet_q.put((CMD_LINE, SOURCE_ADDR))
                info = "Request now in dynet queue."
            else:
                info = "Dynet queue full now."
        elif app == "dlib":
            if dlib_q.qsize() < dlib_q.maxsize:
                dlib_q.put((CMD_LINE, SOURCE_ADDR))
                info = "Request now in dlib queue."
            else:
                info = "Dlib queue full now."

        send_info(info, SOURCE_ADDR)

        if is_vacant(app):
            if app == "opencv":
                CMD_LINE, SOURCE_ADDR = cv_q.get()
                info = "Opencv now working on your request."
            elif app == "dynet":
                CMD_LINE, SOURCE_ADDR = dynet_q.get()
                info = "Dynet now working on your request."
            elif app == "dlib":
                CMD_LINE, SOURCE_ADDR = dlib_q.get()
                info = "Dlib now working on your request."
            send_request(app, CMD_LINE, SOURCE_ADDR)
            send_info(info, SOURCE_ADDR)


if __name__ == "__main__":
    main()