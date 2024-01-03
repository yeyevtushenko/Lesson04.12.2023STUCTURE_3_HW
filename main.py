import queue
import time

class ServerQueue:
    def __init__(self):
        self.request_queue = queue.PriorityQueue()
        self.stats_queue = queue.Queue()

    def addrequest(self, user, priority):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        request = (priority, timestamp, user)
        self.request_queue.put(request)
        print(f"Запит від {user} з пріоритетом {priority} додано до черги.")

    def requests(self):
        while not self.request_queue.empty():
            priority, timestamp, user = self.request_queue.get()
            self.stats_queue.put((timestamp, user))
            print(f"Обробка запиту від {user} з пріоритетом {priority}.")

    def statistics(self):
        print("\nСтатистика обробки запитів:")
        while not self.stats_queue.empty():
            timestamp, user = self.stats_queue.get()
            print(f"{timestamp}: Запит від {user} оброблено.")

def main():
    server = ServerQueue()

    while True:
        print("\nМеню:")
        print("1. Додати новий запит")
        print("2. Обробити запити")
        print("3. Показати статистику")
        print("0. Вийти з програми")

        choice = input("Виберіть опцію (1-3, 0): ")

        if choice == '1':
            user = input("Введіть ім'я користувача: ")
            priority = int(input("Введіть пріоритет (ціле число): "))
            server.addrequest(user, priority)
        elif choice == '2':
            server.requests()
        elif choice == '3':
            server.statistics()
        elif choice == '0':
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()