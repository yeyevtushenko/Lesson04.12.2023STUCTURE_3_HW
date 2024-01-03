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

        def passenger(self):
            arrival_time = self.current_time + random.expovariate(1 / self.arrival_interval)
            stay_time = random.uniform(5, 30)
            passenger = Passenger(arrival_time, stay_time)
            return passenger

        def boat(self):
            arrival_time = self.current_time + random.expovariate(1 / self.boat_interval)
            return arrival_time

        def board_passengers(self, boat):
            free_seats = random.randint(1, boat.capacity)
            boarded_passengers = []
            for _ in range(min(free_seats, self.people_queue.qsize())):
                passenger = self.people_queue.get()
                boarded_passengers.append(passenger)
            return boarded_passengers