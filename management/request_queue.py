import os
import sys
import queue

DEFAULT_QUEUE_SIZE = 6
MANAGEMENT_PORT = 9983
MANAGEMENT_ADDR = "csml-management"
apps = {"opencv":9980, "dynet":9981, "dlib":9982}

class ClientRequestQueue(queue.Queue):
    def __init__(self, app = None , input_maxsize = DEFAULT_QUEUE_SIZE):
        super(ClientRequestQueue, self).__init__(maxsize=input_maxsize)
        self.app = app # type:str
        self.APP_ADDR = "csml-" + self.app # type:str
        self.APP_PORT = apps[self.app] # type:int
        self.input_maxsize = input_maxsize # type:int