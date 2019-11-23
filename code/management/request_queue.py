import os
import sys
import queue
from config import *


class ClientRequestQueue(queue.Queue):
    def __init__(self, app = None, input_maxsize = DEFAULT_QUEUE_SIZE):
        super(ClientRequestQueue, self).__init__(maxsize=input_maxsize)
        self.app = app # type:str
        # Content is just a string

# Maybe unnecessay, the simplest way of sending(sharing)
# files is using docker volume...
class ClientResultQueue(queue.Queue):
    def __init__(self, app = None, input_maxsize = DEFAULT_QUEUE_SIZE):
        super(ClientResultQueue, self).__init__(maxsize=input_maxsize)
        self.app = app