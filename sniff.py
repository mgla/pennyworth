#!/usr/bin/python3
# Simple ARP sniffer to execute actions on specific MAC addresses.
# Author Maik Glatki <maik@glatkieu>

from subprocess import call
import json
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR) # suppress IPV6 warning on startup
from scapy.all import *

print("Scapy initialized")
try:
    with open('/etc/pennyworth/config.json') as data_file:
        config = json.load(data_file)
except FileNotFoundError:
    try:
        with open('examples/config.json') as data_file:
            config = json.load(data_file)
    except FileNotFoundError:
        die("Could not find /etc/pennyworth/config.json or examples/config.json")

playcommand = [config['play']['command']]+config['play']['parameters']

def arp_display(pkt):
    if pkt[ARP].op == 1: #who-has (request)
        if pkt[ARP].psrc == '0.0.0.0': # ARP Probes will match this
            if pkt[ARP].hwsrc in config['macs']:
                print("ARP probe from known devide: " + pkt[ARP].hwsrc)
                call(playcommand + ["resources/audio/test.mp3"])
            else:
                print("ARP Probe from unknown device: " + pkt[ARP].hwsrc)

print(sniff(prn=arp_display, filter="arp", store=0))
