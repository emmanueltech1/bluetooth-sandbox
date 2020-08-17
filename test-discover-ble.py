import asyncio
from bleak import discover

# ----- An UDP client in Python that sends temperature values to server-----
import socket
import random

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT = 12345
buffer=4096

 
# Get temperature
def getTemp():
    temp = random.uniform(60.0, 115.0);
    return temp;

# A tuple with server ip and port
address = (UDP_IP_ADDRESS ,UDP_PORT)

# Create a datagram socket
#tempSensorSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
bleSensorSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);

# Get temperature
temperature = getTemp();
tempString  = "%.2f"%temperature;

# Socket is not in connected state yet...sendto() can be used
# Send temperature to the server
bleSensorSocket.sendto(tempString.encode(), address);

# Read UDP server's response datagram
response = bleSensorSocket.recv(buffer);
print(response);

async def run():
    devices = await discover()
    for d in devices:
        print(d.address, d.name, d.metadata, d.rssi)
        if d.name == "Galaxy Watch (8CEB) LE":
        #if d.address == "3A60299C-2686-44B1-8AB2-788A3D6D6E7C":
            print("Galaxy Watch!!!")
            #print("metadata-uuids %s" %d.metadata['uuids'])
            print("metadata-manufacturer_data %s" %d.metadata['manufacturer_data'])
            print()
            formatter = "%s %s %s %s" % (d.address, d.name, d.metadata, d.rssi)
            bleSensorSocket.sendto(formatter.encode(), address)
            bleResponse = bleSensorSocket.recv(buffer);
            print(bleResponse);
    #formatter = "%s %s %s %s" % (d.address, d.name, d.metadata, d.rssi)
    #bleSensorSocket.sendto(formatter.encode(), address);
    # Read UDP server's response datagram
    #bleResponse = bleSensorSocket.recv(buffer);
    #print(bleResponse);


while (True):
    print()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    print()

# C0:F6:7C:04:B9:D7 Galaxy Watch (8CEB) LE {'uuids': [], 'manufacturer_data': {117: b'\x01\x00\x02\x00\x01\x03\x02'}} -45
# Galaxy Watch!!!
# metadata-uuids []
# metadata-manufacturer {117: b'\x01\x00\x02\x00\x01\x03\x02'}