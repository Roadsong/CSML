import os
import sys
import queue
from config import *


class ClientRequestQueue(queue.Queue):
    def __init__(self, app = None , input_maxsize = DEFAULT_QUEUE_SIZE):
        super(ClientRequestQueue, self).__init__(maxsize=input_maxsize)
        self.app = app # type:str
        self.APP_ADDR = "csml-" + self.app # type:str
        self.APP_PORT = apps[self.app] # type:int