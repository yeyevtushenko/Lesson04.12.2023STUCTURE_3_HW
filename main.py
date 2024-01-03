import random
import time
import queue

class Passenger:
    def __init__(self, arrival_time, stay_time):
        self.arrival_time = arrival_time
        self.stay_time = stay_time