import asyncio
import logging
import websockets

from Communication.Server.CommServerInterface import CommServerInterface


class WebSocketServer(CommServerInterface):
    def __init__(self, config):
        super().__init__(config)
        self._host = self._config.host
        self._port = self._config.port
        self._logger = logging.getLogger(self.__class__.__name__)
        self._websocket_server = None

    def __enter__(self):
        # Concrete implementation for initializing the WebSocket server
        self.server_task = asyncio.ensure_future(self.start_server())
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Concrete implementation for closing the WebSocket server
        asyncio.ensure_future(self.stop_server())

    async def handle_client(self, websocket):
        # Concrete implementation to handle a connected WebSocket client
        self._client_connected(websocket.remote_address)

        try:
            while True:
                message = await websocket.recv()
                if message is None:
                    break  # Connection closed by the client
                self._handle_msg(websocket.remote_address, message)
        except websockets.exceptions.ConnectionClosed:
            pass  # Connection closed by the client

        self._client_disconnected(websocket.remote_address)

    async def start_server(self):
        # Start the WebSocket server
        self._logger.info(f"Starting WebSocket server on {self._host}:{self._port}")
        self._websocket_server = await websockets.serve(
            self.handle_client, self._host, self._port
        )
        await self._websocket_server.wait_closed()

    async def stop_server(self):
        # Stop the WebSocket server
        self._logger.info(f"Stopping WebSocket server on {self._config.host}:{self._config.port}")
        self._websocket_server.close()
        await self._websocket_server.wait_closed()
