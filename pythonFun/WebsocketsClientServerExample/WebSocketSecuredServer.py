import asyncio
import pathlib
import ssl
import websockets

async def handle_message(websocket, path):
    print(f"Client connected from {websocket.remote_address}")

    try:
        while True:
            message = await websocket.recv()
            print(f"Received message from client: {message}")

            response = f"Server received: {message}"
            await websocket.send(response)
            print(f"Sent response to client: {response}")

    except websockets.exceptions.ConnectionClosed:
        print(f"Connection closed by {websocket.remote_address}")

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(
    pathlib.Path('cert.pem'),
    pathlib.Path('key.pem')
)

port = 8765
# Start the encrypted WebSocket server
start_server = websockets.serve(
    handle_message,
    "localhost",
    port,
    ssl=ssl_context
)
print(f"running server on port {port}")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
