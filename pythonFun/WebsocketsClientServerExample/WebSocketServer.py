import asyncio
import websockets


async def handle_message(websocket):
    # This function will be called whenever a new WebSocket connection is established
    print(f"Client connected from {websocket.remote_address}")

    try:
        while True:
            # Wait for a message from the client
            message = await websocket.recv()
            print(f"Received message from client: {message}")

            # Send a response back to the client
            response = f"Server received: {message}"
            await websocket.send(response)
            print(f"Sent response to client: {response}")

    except websockets.exceptions.ConnectionClosed:
        print(f"Connection closed by {websocket.remote_address}")


# Start the WebSocket server
start_server = websockets.serve(handle_message, "127.0.0.1", 8765)

# Run the event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
