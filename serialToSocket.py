import serial
import asyncio
import websockets
import json

ser = serial.Serial('/dev/cu.usbmodem14101', 9600)


async def echoSerial(websocket, path):
    while asyncio.get_event_loop().is_running():
        await websocket.send(json.dumps({'blink': ser.readline().decode().strip()}))

start_server = websockets.serve(echoSerial, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
