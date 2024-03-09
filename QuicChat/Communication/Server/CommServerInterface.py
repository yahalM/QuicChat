from abc import ABC, abstractmethod


class CommServerInterface(ABC):
    def __init__(self, config):
        # Initialize communication parameters (e.g., URI for WebSocket connection)
        self._config = config
        self._handle_msg = config.client_handler.handle_msg
        self._client_connected = config.client_handler.client_connected
        self._client_disconnected = config.client_handler.client_disconnected

    @abstractmethod
    def __enter__(self):
        # Enter method (constructor) - initialize the communication connection
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        # Exit method (destructor) - close the communication connection
        pass

