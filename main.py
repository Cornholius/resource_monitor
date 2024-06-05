import psutil
import os
from time import sleep


class Size:
    kb = 1024
    mb = 1048576
    gb = 1073741824


class Disk(Size):
    def __init__(self, drive, total, used, free, percent):
        self.drive = drive
        self.total = total // self.gb
        self.used = used // self.gb
        self.free = free // self.gb
        self.percent = percent

    def __str__(self):
        return f'drive {self.drive}'


class System(Size):

    def get_ram(self):
        """
        Получает данные о памяти и возвращает словарь
        :return: {total: int, used: float, free: float, percent: int}
        """
        memory = psutil.virtual_memory()
        total = int(memory.total / self.gb)
        used = round(memory.used / self.gb, 2)
        free = round(memory.available / self.gb, 2)
        percent = int(memory.percent)
        return {'total': total, 'used': used, 'free': free, 'percent': percent}

    def get_cpu(self):
        return psutil.cpu_percent(interval=0.5)

    def get_loadavg(self):
        return psutil.getloadavg()

    def get_discs(self):
        devices = []

        for device in psutil.disk_partitions():
            volume = psutil.disk_usage(device.device)
            devices.append(Disk(device.device[0], volume.total, volume.used, volume.free, int(volume.percent)))

        return devices


ram = System()
for i in ram.get_discs():
    print(f'Диск {i.drive}, Всего {i.total} Гб')
    print(f'Занято {i.used} Гб // Свободно {i.free} Гб ({i.percent}%)')
    print(f"{'▓' * (i.percent // 2) + '░' * (50 - i.percent // 2)}")
