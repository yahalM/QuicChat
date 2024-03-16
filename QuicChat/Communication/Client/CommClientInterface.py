from abc import ABC, abstractmethod


class CommInterface(ABC):
    def __init__(self, config):
        # Initialize communication parameters (e.g., URI for WebSocket connection)
        self._config = config

    @abstractmethod
    async def open_connection(self):
        # Abstract method to open the communication connection
        pass

    @abstractmethod
    async def close_connection(self):
        # Abstract method to close the communication connection
        pass

    @abstractmethod
    async def send_message(self, message):
        # Abstract method to send a message
        pass

    @abstractmethod
    async def receive_message(self):
        # Abstract method to receive a message
        pass