import random
import time
import queue

class Passenger:
    def __init__(self, arrival_time, stay_time):
        self.arrival_time = arrival_time
        self.stay_time = stay_time

class BoatStop:
    def __init__(self, arrival_interval, boat_interval, stop_type, max_people):
        self.arrival_interval = arrival_interval
        self.boat_interval = boat_interval
        self.stop_type = stop_type
        self.max_people = max_people
        self.people_queue = queue.Queue()
        self.boats_at_stop = []
        self.current_time = 0
