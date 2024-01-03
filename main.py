import random
import datetime
import queue

class Passenger:
    def __init__(self, arrival_time, stay_time):
        self.arrival_time = arrival_time
        self.stay_time = stay_time

class BoatStop:
    def __init__(self, arrival_interval, boat_interval, stop_type, max_people, capacity):
        self.arrival_interval = arrival_interval
        self.boat_interval = boat_interval
        self.stop_type = stop_type
        self.max_people = max_people
        self.capacity = capacity
        self.people_queue = queue.Queue()
        self.boats_at_stop = []
        self.current_time = 0

        # Змінні для статистики
        self.total_passenger_stay_time = 0
        self.total_passengers_served = 0
        self.total_boat_intervals = 0
        self.total_free_seats = 0

    def passenger(self):
        arrival_time = self.current_time + random.expovariate(1 / self.arrival_interval)
        stay_time = random.uniform(5, 30)
        passenger = Passenger(arrival_time, stay_time)
        return passenger

    def boat(self):
        arrival_time = self.current_time + random.expovariate(1 / self.boat_interval)
        return arrival_time

    def board_passengers(self, boat):
        free_seats = random.randint(1, min(self.capacity, self.people_queue.qsize()))
        boarded_passengers = []
        for _ in range(free_seats):
            passenger = self.people_queue.get()
            boarded_passengers.append(passenger)
            self.total_passenger_stay_time += passenger.stay_time
            self.total_passengers_served += 1

        self.total_free_seats += (self.capacity - free_seats)
        return boarded_passengers

    def run(self, simulation_time):
        while self.current_time < simulation_time:
            passenger = self.passenger()
            self.people_queue.put(passenger)

            if self.stop_type == "final" and random.random() < 0.1:
                boat = self.boat()
                boarded_passengers = self.board_passengers(boat)
                print(f"Катер {boat} прибув на кінцеву зупинку. "
                      f"Пасажири {boarded_passengers} сіли на борт.")
            else:
                formatted_time = datetime.datetime.fromtimestamp(passenger.arrival_time).strftime('%H:%M:%S')
                print(f"Пасажир прибув на зупинку о {formatted_time}. Тип зупинки: {self.stop_type}")

            self.current_time += passenger.arrival_time

            if self.stop_type == "final":
                self.total_boat_intervals += 1
                self.total_free_seats += self.capacity

    def statistics(self):
        average_stay_time = self.total_passenger_stay_time / self.total_passengers_served if self.total_passengers_served > 0 else 0
        average_boat_interval = self.current_time / self.total_boat_intervals if self.total_boat_intervals > 0 else 0
        average_free_seats = self.total_free_seats / self.total_boat_intervals if self.total_boat_intervals > 0 else 0

        print(f"Середній час перебування пасажира на зупинці: {average_stay_time:.2f} хвилин")
        print(f"Середній інтервал між приходами катерів: {average_boat_interval:.2f} хвилин")
        print(f"Середня кількість вільних місць у катерах: {average_free_seats:.2f}")

if __name__ == "__main__":
    arrival_interval = float(input("Введіть середній інтервал прибуття пасажирів (у хвилинах): "))
    boat_interval = float(input("Введіть середній інтервал прибуття катерів (у хвилинах): "))
    simulation_time = float(input("Введіть час симуляції (у хвилинах): "))
    stop_type = input("Введіть тип зупинки (final або intermediate): ")
    max_people = int(input("Введіть максимальну кількість пасажирів на зупинці: "))
    boat_capacity = int(input("Введіть кількість місць у катері: "))

    stop = BoatStop(arrival_interval=arrival_interval, boat_interval=boat_interval,
                    stop_type=stop_type, max_people=max_people, capacity=boat_capacity)
    stop.run(simulation_time)
    stop.statistics()
