import serial, time
arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(1) #give the connection a second to settle
# arduino.write("Hello from Python!")
while True:
#     data = arduino.read()
    data = arduino.readline()
    data = data[:12]
    print data

        
