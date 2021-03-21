#!/bin/bash

sudo apt-get install qt5-default -y
sudo apt-get install sip-dev -y

cd /usr/src
sudo wget https://www.riverbankcomputing.com/static/Downloads/sip/4.19.25/sip-4.19.25.tar.gz
sudo tar xzf sip-4.19.25.tar.gz
cd sip-4.19.25
sudo python3.7 configure.py --sip-module PyQt5.sip
sudo make
sudo make install

cd /usr/src
sudo wget https://files.pythonhosted.org/packages/8e/a4/d5e4bf99dd50134c88b95e926d7b81aad2473b47fde5e3e4eac2c69a8942/PyQt5-5.15.4.tar.gz
cd PyQt5-5.15.4
sudo python3.7 configure.py
sudo make
sudo make install
