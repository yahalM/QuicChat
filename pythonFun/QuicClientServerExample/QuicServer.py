import asyncio
from aioquic.asyncio import serve
from aioquic.asyncio.protocol import QuicConnectionProtocol
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import StreamDataReceived

class EchoQuicProtocol(QuicConnectionProtocol):
    def quic_event_received(self, event):
        if isinstance(event, StreamDataReceived):
            # Echo back any received data
            print(f"Received: {event.data.decode()} let's echo!")
            self._quic.send_stream_data(event.stream_id, event.data)
            if event.end_stream:
                self._quic.send_stream_data(event.stream_id, b'', end_stream=True)
 
async def run_server():
    # Server configuration
    config = QuicConfiguration(is_client=False)
    config.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
 
    # Bind the QUIC server to localhost on port 4433
    server = await serve('localhost', 4433, configuration=config, create_protocol=EchoQuicProtocol)
 
    try:
        # Keep the server running indefinitely
        await asyncio.Future()  # This future never completes
    except asyncio.CancelledError:
        # Properly close the server when the future is cancelled
        server.close()
        await server.wait_closed()
 
# Run the server
print("running")
asyncio.run(run_server())
print("dead!")