import queue
import time

class ServerQueue:
    def __init__(self):
        self.request_queue = queue.PriorityQueue()
        self.stats_queue = queue.Queue()