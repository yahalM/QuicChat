import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Send a message to the server
        message = "Hello, WebSocket Server From YM!"
        await websocket.send(message)
        print(f"Sent message to server: {message}")

        # Receive and print the server's response
        response = await websocket.recv()
        print(f"Received response from server: {response}")

# Run the WebSocket client
asyncio.get_event_loop().run_until_complete(send_message())
