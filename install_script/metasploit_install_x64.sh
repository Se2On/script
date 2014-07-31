#!/bin/bash
sudo apt-get install ruby1.9.1 build-essential
wget http://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run
sudo chmod +x metasploit-latest-linux-x64-installer.run
sudo ./metasploit-latest-linux-x64-installer.run
rm metasploit-lastest-linux-x64-installer.run
