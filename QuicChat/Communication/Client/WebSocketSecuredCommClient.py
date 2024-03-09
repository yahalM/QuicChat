import websockets
import logging
from Communication.Client.CommClientInterface import CommClientInterface


class WebSocketCommClient(CommClientInterface):
    def __init__(self, config):
        super().__init__(config)
        self._websocket = None
        self._logger = logging.getLogger(self.__class__.__name__)

    async def open_connection(self):
        # Concrete implementation to open a WebSocket connection
        self._logger.info(f"Opening secured WebSocket connection to {self._config.uri}")
        self._websocket = await websockets.connect(self._config.uri, ssl=self._config.ssl_context)

    async def close_connection(self):
        # Concrete implementation to close the WebSocket connection
        self._logger.info(f"Closing secured WebSocket connection to {self._config.uri}")
        await self._websocket.close()

    async def send_message(self, message):
        # Concrete implementation to send a message via WebSocket
        self._logger.info(f"Sending message to {self._config.uri} via secured WebSocket: {message}")
        await self._websocket.send(message)

    async def receive_message(self):
        # Concrete implementation to receive a message via WebSocket
        received_message = await self._websocket.recv()
        self._logger.info(f"Received message from {self._config.uri} via secured WebSocket: {received_message}")
        return received_message
