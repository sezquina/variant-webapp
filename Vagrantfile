# -*- mode: ruby -*-
# vi: set ft=ruby :

$DOCKER = <<SCRIPT
  sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
  sudo echo 'deb https://apt.dockerproject.org/repo ubuntu-wily main' > /etc/apt/sources.list.d/docker.list
  sudo apt-get update

  sudo apt-get install linux-image-extra-$(uname -r) -y
  sudo apt-get install docker-engine docker-compose -y

  sudo service docker start
SCRIPT

$ANSIBLE = <<SCRIPT
  sudo apt-get install software-properties-common -y
  sudo apt-add-repository ppa:ansible/ansible -y
  sudo apt-get update

  sudo easy_install pip
  sudo pip install virtualenv

  sudo apt-get install ansible -y
SCRIPT

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/wily64"
  config.vm.box_version = "20151120.0.0"
  
  config.vm.network "forwarded_port", guest: 5000, host: 5000 # Flask
  config.vm.network "forwarded_port", guest: 5432, host: 5432 # PostgreSQL
  config.vm.network "forwarded_port", guest: 8000, host: 8000 # Gunicorn
  config.vm.network "forwarded_port", guest: 8080, host: 8080 # HTTP Alternative

  config.vm.network "private_network", ip: "10.1.0.10"

  config.vm.provider "virtualbox" do |vb|
      vb.memory = "4096"  
  end

  config.vm.provision :shell, privileged: true, :inline => $DOCKER
  #config.vm.provision :shell, privileged: true, :inline => $ANSIBLE
end
