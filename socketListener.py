import asyncio
import websockets


async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:
        state = await websocket.recv()
        print(state)


asyncio.run(hello())
