# -*- mode: ruby -*-

VAGRANTFILE_API_VERSION = "2"
hostname_prefix = 'local01-'
domain = 'local'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "pennyworth" do |master|
    master.vm.box      = "debian/contrib-jessie64"
    master.vm.box_url  = "https://atlas.hashicorp.com/debian/contrib-jessie64"
    master.vm.hostname = "local01-pennyworth.#{domain}"
    master.vm.network    "private_network", ip: "192.168.33.10"
    master.vm.provision :hosts, :sync_hosts => true
    master.vm.provision :shell, :path => "vagrant/system-prep-deb.sh"
    master.vm.synced_folder ".", "/opt/pennyworth", create: true
    master.vm.provider "virtualbox" do |vb|
      vb.customize ["modifyvm", :id, "--memory", "1024", "--cpus", "1", "--ioapic", "on"]
    end
  end

# vi: set ft=ruby :
