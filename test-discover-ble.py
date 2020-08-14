import asyncio
from bleak import discover

# ----- An UDP client in Python that sends temperature values to server-----
import socket
import random

 
# Get temperature
def getTemp():
    temp = random.uniform(60.0, 115.0);
    return temp;

# A tuple with server ip and port
serverAddress = ("127.0.0.1", 7070);

# Create a datagram socket
#tempSensorSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
bleSensorSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);

# Get temperature
#temperature = getTemp();
#tempString  = "%.2f"%temperature;

# Socket is not in connected state yet...sendto() can be used
# Send temperature to the server
#tempSensorSocket.sendto(tempString.encode(), ("127.0.0.1",7070));

# Read UDP server's response datagram
#response = tempSensorSocket.recv(1024);
#print(response);

async def run():
    devices = await discover()
    for d in devices:
        print(d.address, d.name, d.metadata, d.rssi)
        if d.name == "Galaxy Watch (8CEB) LE":
            print("Galaxy Watch!!!")
            print("metadata-uuids %s" %d.metadata['uuids'])
            print("metadata-manufacturer_data %s" %d.metadata['manufacturer_data'])
            print()
    formatter = "%s %s %s %s" % (d.address, d.name, d.metadata, d.rssi)
    bleSensorSocket.sendto(formatter.encode(), ("127.0.0.1",7070));
    # Read UDP server's response datagram
    bleResponse = bleSensorSocket.recv(1024);
    print(bleResponse);


while (True):
    print()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
    print()

# C0:F6:7C:04:B9:D7 Galaxy Watch (8CEB) LE {'uuids': [], 'manufacturer_data': {117: b'\x01\x00\x02\x00\x01\x03\x02'}} -45
# Galaxy Watch!!!
# metadata-uuids []
# metadata-manufacturer {117: b'\x01\x00\x02\x00\x01\x03\x02'}