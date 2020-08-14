#!/usr/bin/env python
#--*--coding:UTF-8 --*--

# ----- An UDP server in Python that receives temperature values from clients-----
import socket
import datetime

# Define the IP address and the Port Number
ip      = "127.0.0.1";
port    = 7070;
listeningAddress = (ip, port);

# Create a datagram based server socket that uses IPv4 addressing scheme
datagramSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
datagramSocket.bind(listeningAddress);

while(True):
    #address, name, metadata, rssi = datagramSocket.recvfrom(1024);
    address, name = datagramSocket.recvfrom(1024);
    #print("BLE data: %s  %s  %s  %s"%(address, name, metadata, rssi));
    print("BLE data: %s  %s"%(address, name));
    response = "Received at: %s"%datetime.datetime.now();
    datagramSocket.sendto(response.encode(), (address, name));