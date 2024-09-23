import serial
import serial.tools.list_ports as port_list

ports = list(port_list.comports())
for p in ports:
    print (p)

serialPort = serial.Serial(
    port="COM4",
    baudrate=115200,
    bytesize=8,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=100
)

serialPort.write((10).to_bytes(1, "big"))

# while 1:
    # serialStr = serialPort.readline()
    # print(serialStr.decode("Ascii"))