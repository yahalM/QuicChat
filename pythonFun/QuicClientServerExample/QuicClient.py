import asyncio
from aioquic.asyncio import connect
from aioquic.asyncio.protocol import QuicConnectionProtocol
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import StreamDataReceived
import ssl

class EchoQuicProtocol(QuicConnectionProtocol):
    def quic_event_received(self, event):
        if isinstance(event, StreamDataReceived):
            print(f"Received: {event.data.decode()}")
            
async def run():
    config = QuicConfiguration(is_client=True)
    config.verify_mode = ssl.CERT_NONE# For testing purposes; in production, you should verify the certificate

    async with connect('localhost', 4433, configuration=config, create_protocol=EchoQuicProtocol) as connection:
        for i in range(5):
            stream_id = connection._quic.get_next_available_stream_id()
            # Send a message
            connection._quic.send_stream_data(stream_id, f'Hello, QUIC Server - {i}'.encode('utf-8'), end_stream=True)

        # Wait a bit for the response
        await asyncio.sleep(1)

asyncio.run(run())