# Arduino/Raspberry Pi Serial to WebSockets

[blinkSerialOutput.ino](blinkSerialOutput.ino) is the Arduino file with the blink and serial output code.

You can download the [IDE](https://www.arduino.cc/en/Main/Software) or use the [web version](https://create.arduino.cc/editor) to flash the board.

[readSerial.py](readSerial.py) Will give you basic serial monitor output in python when pointed at the right usb port.

[serialToSocket.py](serialToSocket.py) will take the serial output from the Arduino and pass it to a [WebSocket](https://en.wikipedia.org/wiki/WebSocket).

[socketListener.py](socketListener.py) is a Python method for listening to the WebSocket.

We can listen to the WebSocket in the browser so we can print and change the state. You can see an example of this in [index.html](index.html).
