# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.define "fserver" do |fserver|
    fserver.vm.box = "generic/ubuntu1804"
    fserver.vm.hostname = "fserver"
    fserver.vm.network "private_network", ip: "192.168.56.5"
    fserver.vm.provision "shell", inline: "mkdir -p /Workspace /Workspace/data; cd /Workspace; wget -q https://dl.min.io/server/minio/release/linux-amd64/minio; chmod u+x minio"
    fserver.vm.provision "shell", inline: "screen -dm bash -c 'cd /Workspace; export MINIO_ROOT_USER=fuser; export MINIO_ROOT_PASSWORD=h38KGSCII9YASmRy5zjq; ./minio server /Workspace/data --console-address \":9001\" --address \":9002\"'", run: 'always'
    fserver.vm.provision "shell", inline: "cd /Workspace; wget -q https://dl.min.io/client/mc/release/linux-amd64/mc; chmod u+x mc; ./mc alias set fserver http://192.168.56.5:9002/ fuser h38KGSCII9YASmRy5zjq"
    fserver.vm.provision "shell", inline: "cd /Workspace; git clone https://github.com/haward79/nycu_cloud_system_3-tier_website.git"
    fserver.vm.provision "shell", inline: "cd /Workspace; ./mc mb fserver/frontend; ./mc mirror /Workspace/nycu_cloud_system_3-tier_website/frontend fserver/frontend"
    fserver.vm.provision "shell", inline: "cd /Workspace; ./mc mb fserver/public; ./mc mirror /Workspace/nycu_cloud_system_3-tier_website/frontend/static/ fserver/public; ./mc anonymous set download fserver/public"
    fserver.vm.provision "shell", inline: "rm -r /Workspace/nycu_cloud_system_3-tier_website"
  end
  
  config.vm.define "mysql" do |mysql|
    mysql.vm.box = "generic/ubuntu2004"
    mysql.vm.hostname = "mysql"
    mysql.vm.network "private_network", ip: "192.168.56.4"
    mysql.vm.provision "shell", inline: "apt update; apt install -y mysql-server"
    mysql.vm.provision "shell", inline: "mkdir -p /Workspace; cd /Workspace; git clone https://github.com/haward79/nycu_cloud_system_3-tier_website.git"
    mysql.vm.provision "shell", inline: "cd /Workspace/nycu_cloud_system_3-tier_website; chmod u+x mysql_secure_setup; ./mysql_secure_setup"
  end
  
  config.vm.define "backend" do |backend|
    backend.vm.box = "generic/ubuntu2004"
    backend.vm.hostname = "backend"
    backend.vm.network "private_network", ip: "192.168.56.3"
    backend.vm.provision "shell", inline: "apt update; apt install -y python3-pip; pip install -U Flask flask-cors mysql-connector-python"
    backend.vm.provision "shell", inline: "mkdir -p /Workspace; cd /Workspace; git clone https://github.com/haward79/nycu_cloud_system_3-tier_website.git"
    backend.vm.provision "shell", inline: "screen -dm bash -c 'cd /Workspace/nycu_cloud_system_3-tier_website/backend; flask --app main --debug run --host=0.0.0.0'", run: 'always'
  end
  
  config.vm.define "frontend" do |frontend|
    frontend.vm.box = "generic/ubuntu2004"
    frontend.vm.hostname = "frontend"
    frontend.vm.network "private_network", ip: "192.168.56.2"
    frontend.vm.provision "shell", inline: "apt update; apt install -y python3-pip; pip install -U Flask"
    frontend.vm.provision "shell", inline: "mkdir -p /Workspace; cd /Workspace"
    frontend.vm.provision "shell", inline: "cd /Workspace; wget -q https://dl.min.io/client/mc/release/linux-amd64/mc; chmod u+x mc; bash +o history; ./mc alias set fserver http://192.168.56.5:9002/ fuser h38KGSCII9YASmRy5zjq; bash -o history"
    frontend.vm.provision "shell", inline: "cd /Workspace; ./mc cp --recursive fserver/frontend /Workspace/nycu_cloud_system_3-tier_website; rm -r /Workspace/nycu_cloud_system_3-tier_website/frontend/static"
    frontend.vm.provision "shell", inline: "screen -dm bash -c 'cd /Workspace/nycu_cloud_system_3-tier_website/frontend; flask --app main --debug run --host=0.0.0.0'", run: 'always'
  end

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
end
