import os
import sys
import socket
from config import *

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind(("csml-dlib", apps["dlib"]))

def main():
    # (simplest) CMD_LINE Format
    # app:container_id:simple_request
    while True:

        CMD_LINE, SOURCE_ADDR = serverSock.recvfrom(1024)
        container_id = CMD_LINE.split(":")[1] # type:str
        simple_request = CMD_LINE.split(":")[2] # type:bool

        # Ready to process, change the status to [pending]
        # If first use, ignore the error anyway, no harm
        EXE_LINE = "mv /results/opencv/" + str(container_id) + ".log /results/dlib/[pending]" + str(container_id) + ".log"
        os.system(EXE_LINE)

        if simple_request:
            EXE_LINE = "/dlib-19.18/examples/build/svm_ex"
            EXE_LINE += " | ts '[%Y-%m-%d %H:%M:%S]'"
            EXE_LINE += " | tee -a /results/dlib/[pending]" # -a for appending
            EXE_LINE += str(container_id) + ".log" # One user one .log file
            os.system(EXE_LINE)

        # Remove the [pending] status
        EXE_LINE = "mv /results/dlib/[pending]" + str(container_id) + ".log /results/dlib/" + str(container_id) + ".log"
        os.system(EXE_LINE)

if __name__ == "__main__":
    main()