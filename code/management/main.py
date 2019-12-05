import os
import socket
import sys

import request_queue
from config import *

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((MANAGEMENT_ADDR, MANAGEMENT_PORT))


# Check the target app is vacant or not
# How to check? Cannot use cpu indicator because resources are shared!
def is_vacant(app):
    # grep [pending] in filename would be fine
    EXE_LINE = "ls /results/opencv/ | grep [pending] > /tmp/" + str(app) + "grep_results"
    os.system(EXE_LINE)
    if os.stat("/tmp/" + str(app) + "_grep_results").st_size == 0:
        return True
    else:
        return False


# Send request to target app
def send_request(app, CMD_LINE):
    APP_ADDR = "csml-" + app # type:str
    APP_PORT = apps[app] # type:int

    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSock.sendto(CMD_LINE, (APP_ADDR, APP_PORT))
    clientSock.close()


# Send back useful information to user
def send_info(info, SOURCE_ADDR):
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

        CMD_LINE = ""
        SOURCE_ADDR = ""

        serverSock.setblocking(0) # Non-blocking
        CMD_LINE, SOURCE_ADDR = serverSock.recvfrom(1024)
        
        if CMD_LINE and SOURCE_ADDR: # Received a new request
            
            print("Received a request.")
            
            # (simplest) Format
            # app:container_id:simple_request
            app = CMD_LINE.split(":")[0] # type:str

            if app == "opencv":
                if cv_q.qsize() < cv_q.maxsize:
                    cv_q.put(CMD_LINE)
                    info = "Request now in opencv queue."
                else:
                    info = "Opencv queue full now."
            elif app == "dynet":
                if dynet_q.qsize() < dynet_q.maxsize:
                    dynet_q.put(CMD_LINE)
                    info = "Request now in dynet queue."
                else:
                    info = "Dynet queue full now."
            elif app == "dlib":
                if dlib_q.qsize() < dlib_q.maxsize:
                    dlib_q.put(CMD_LINE)
                    info = "Request now in dlib queue."
                else:
                    info = "Dlib queue full now."

            send_info(info, SOURCE_ADDR)

        # Running silently can avoid lots of work :)
        # If any of a app is vacant and there is a request in queue
        if is_vacant("opencv") and not cv_q.empty():
            CMD_LINE = cv_q.get()
        if is_vacant("dynet") and not dynet_q.empty():
            CMD_LINE = dynet_q.get()
        if is_vacant("dlib") and not dlib_q.empty():
            CMD_LINE = dlib_q.get()
        
        # Just do it 
        if CMD_LINE:
            send_request(app, CMD_LINE)


if __name__ == "__main__":
    main()
