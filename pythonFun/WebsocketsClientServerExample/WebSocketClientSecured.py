import asyncio
import websockets
import ssl

async def send_message():
    uri = "wss://localhost:8765"

    # Disable certificate verification for testing purposes
    ssl_context = ssl.SSLContext()
    ssl_context.verify_mode = ssl.CERT_NONE

    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        # Send a message to the server
        message = "Hello, WebSocket Server From YM!"
        await websocket.send(message)
        print(f"Sent message to server: {message}")

        # Receive and print the server's response
        response = await websocket.recv()
        print(f"Received response from server: {response}")

# Run the WebSocket client
asyncio.get_event_loop().run_until_complete(send_message())
