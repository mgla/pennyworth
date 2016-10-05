## Installation

You need to ensure yourself that you can play audio files.

* For virtualized environments, I recommend sox with libsox-fmt-mp3.
* For Raspberry Pis with Rasbian, I recommend omxplayer. Install with

    sudo apt-get -y install omxplayer

For user execution, execute:

    chmod a+rw /dev/vchiq

## Usage

TBD.

## Development

Quick overview:

* vagrant up
* ssh into VM with either `vagrant ssh` or directly.
* Go to /home/vagrant/pennyworth
* ./manage.py runserver 0.0.0.0:8000

### Vagrant

Install vagrant and a virtualization provider.

* For Vagrant, see https://www.vagrantup.com
* For virtualization, you can use VirtualBox, see https://www.virtualbox.org/wiki/Downloads

Clone repository, Code like hell, Push, open pull request.
