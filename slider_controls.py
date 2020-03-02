import serial

def send(data):
    print(data)
    port.write(data) 
    while True:
        response=port.read(33)
        print("Rx:"+response)
        break

port =serial.Serial(
    "/dev/ttyUSB0",
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    writeTimeout = 0,
    timeout = 1)


if port.isOpen():
    print("Port opened...")
else:
    print("Port did not open")

send("Tx:0in")

print("Initialization...")
port.write("Tx:1in")
port.write("Tx:2in")
port.write("Tx:3in")
port.write("Tx:4in")
port.write("Tx:5in")
port.write("Tx:6in")
port.write("Tx:7in")
port.write("Tx:8in")
port.write("Tx:9in")
port.write("Tx:Ain")
port.write("Tx:Bin")
port.write("Tx:Cin")
port.write("Tx:Din")
port.write("Tx:Ein")
port.write("Tx:Fin")

send("Tx:0i1")

#print("Move device to 0.0 mm")
#send("Tx:0ma00000000")    
#print("Move device to 32.0 mm")
#send("Tx:0ma00000020")
#print("Move device to 64.0 mm")
#send("Tx:0ma00000040")
#print("Move device to 96.0 mm")
#send("Tx:0ma00000060")
#print("Homing device")
#send("0ho0")

def home():
    print("Homing device")
    send("0ho0")
def pos(i):
    if i==0:
        print("Move device to 0.0 mm")
        send("Tx:0ma00000000")   
    elif i==1:
        print("Move device to 32.0 mm")
        send("Tx:0ma00000020")
    elif i==2:
        print("Move device to 64.0 mm")
        send("Tx:0ma00000040")
    elif i==3:
        print("Move device to 96.0 mm")
        send("Tx:0ma00000060")

