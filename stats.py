import os
from abc import abstractmethod

import psutil


class Stats:
    def __init__(self, client):
        self.client = client
        self.process = psutil.Process(os.getpid())

    @abstractmethod
    def library_info(self) -> str:
        ...

    @abstractmethod
    def server_count(self) -> int:
        ...

    @abstractmethod
    def total_users(self) -> int:
        ...

    def average_users(self) -> float:
        return round(self.total_users() / self.server_count())

    def process_ram_usage(self) -> str:
        return f"{self.process.memory_full_info().rss / 1024 ** 2:.2f} MB"

    def cpu_count(self) -> int:
        return psutil.cpu_count()

    def process_cpu_usage(self) -> float:
        process_cpu_usage = self.process.cpu_percent()
        return process_cpu_usage if process_cpu_usage <= 100 else process_cpu_usage / self.cpu_count

    def server_cpu_usage(self) -> float:
        server_cpu_usage = psutil.cpu_percent()
        return server_cpu_usage if server_cpu_usage <= 100 else server_cpu_usage / self.cpu_count

    def server_ram_usage(self) -> str:
        return f"{psutil.virtual_memory().used / 1024 / 1024:.0f} MB"

    def __str__(self):
        return (
            f"Library: {self.library_info()}\n"
            f"Server count: {self.server_count()}\n"
            f"Total users: {self.total_users()}\n"
            f"Average users: {self.average_users()}\n\n"

            f"Process RAM usage: {self.process_ram_usage()}\n"
            f"Server RAM usage: {self.server_ram_usage()}\n"
            f"Process CPU usage: {self.process_cpu_usage()}\n"
            f"Server CPU usage: {self.process_cpu_usage()}\n"
        )
