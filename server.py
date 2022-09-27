SERVERS = []
ROUTERS = []


class Server:
    """для описания работы серверов в сети
    Соответственно в объектах класса Server должны быть локальные свойства:
    buffer - список принятых пакетов (изначально пустой);
    ip - IP-адрес текущего сервера.
    """

    counter = 0  # Генерация IP-адреса при создании экз. класса

    def __new__(cls, *args, **kwargs):
        cls.counter += 1
        return super().__new__(cls)

    def __init__(self):
        self.buffer = []
        self.IP = self.counter
        SERVERS.append(self)

    def send_data(self, data):
        """для отправки информационного пакета data (объекта класса Data)
        с указанным IP-адресом получателя (пакет отправляется роутеру и
        сохраняется в его буфере - локальном свойстве buffer);
        """
        for router in ROUTERS:
            if self in router.CONNECTED_SERVERS:
                router.buffer.insert(0, data)

    def get_data(self):
        """возвращает список принятых пакетов (если ничего принято не было,
        то возвращается пустой список) и очищает входной буфер;
        """
        temp = self.buffer.copy()
        self.buffer.clear()
        return temp

    def get_ip(self):
        """возвращает свой IP-адрес.
        """
        return self.IP


class Router:
    """для описания работы роутеров в сети (в данной задаче полагается один роутер).
    И одно обязательное локальное свойство (могут быть и другие свойства):
    buffer - список для хранения принятых от серверов пакетов (объектов класса Data).
    """
    CONNECTED_SERVERS = []
    buffer = []
    router_number = 0

    def __new__(cls, *args, **kwargs):
        cls.router_number += 1
        return super().__new__(cls)

    def __init__(self):
        self.ROUTER_IP = self.router_number
        ROUTERS.append(self)

    def link(self, server):
        """для присоединения сервера server (объекта класса Server) к роутеру
        """
        if server not in self.CONNECTED_SERVERS:
            self.CONNECTED_SERVERS.append(server)

    def unlink(self, server):
        """для отсоединения сервера server (объекта класса Server) от роутера
        """
        if server in self.CONNECTED_SERVERS:
            self.CONNECTED_SERVERS.remove(server)

    def send_data(self):
        """для отправки всех пакетов (объектов класса Data) из буфера роутера
        соответствующим серверам (после отправки буфер должен очищаться)
        """
        while self.buffer:
            data = self.buffer.pop()
            for server in self.CONNECTED_SERVERS:
                if data.ip == server.IP:  # Проверяем есть ли данные для передачи к подключенным серверам
                    server.buffer.insert(0, data)

class Data:
    """для описания пакета информации
    Наконец, объекты класса Data должны содержать, два следующих локальных свойства:
    data - передаваемые данные (строка);
    ip - IP-адрес назначения.
    """

    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip