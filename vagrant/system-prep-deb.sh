#!/bin/bash
export DEBIAN_FRONTEND=noninteractive

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y

# Developer tools
sudo apt-get install vim
# Dependencies
sudo apt-get install -y sox libsox-fmt-mp3 tcpdump python3 python3-pip
sudo pip3 install scapy-python3
