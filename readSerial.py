import serial

ser = serial.Serial('/dev/cu.usbmodem4013101', 9600)

while True:
    print(ser.readline())
