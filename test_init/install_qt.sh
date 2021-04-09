#!/bin/bash

sudo apt-get install qt5-default -y

pip3 install PyQt5-sip
pip3 install pygame
pip3 install pyqt5

sudo apt-get install qt5-default -y
sudo apt-get install sip-dev -y

wget https://www.riverbankcomputing.com/static/Downloads/sip/4.19.25/sip-4.19.25.tar.gz
tar xzf sip-4.19.25.tar.gz
cd sip-4.19.25
python3 configure.py --sip-module PyQt5.sip
make
sudo make install

cd ..
rm -r sip-4.19.25*

wget https://files.pythonhosted.org/packages/8e/a4/d5e4bf99dd50134c88b95e926d7b81aad2473b47fde5e3e4eac2c69a8942/PyQt5-5.15.4.tar.gz
tar xzf PyQt5-5.15.4.tar.gz
cd PyQt5-5.15.4
python3 configure.py
make
sudo make install

cd ..
rm -r PyQt5-5.15.4*
