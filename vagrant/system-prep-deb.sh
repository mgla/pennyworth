#!/bin/bash
export DEBIAN_FRONTEND=noninteractive

sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y

## Developer tools
# Specific to this project
sudo apt-get install -y sqllite3
# Common
sudo apt-get install -y vim git
# Some of my more personal stuff. Comment it out if you do not like it
sudo apt-get install -y zsh tree tmux curl
pushd ~
git clone https://github.com/mgla/dotfiles && ./dotfiles/deploy
popd
sudo chsh vagrant -s /bin/zsh

## Dependencies
sudo apt-get install -y sox libsox-fmt-mp3 tcpdump python3 python3-pip
sudo pip3 install scapy-python3 Django==1.10.1
