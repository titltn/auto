#!/usr/bin/python3

import os

os.system('sudo apt-get update')
os.system('sudo apt-get install ca-certificates curl gnupg lsb-release')
os.system('sudo mkdir -p /etc/apt/keyrings')
os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg')
os.system('echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
os.system('sudo chmod a+r /etc/apt/keyrings/docker.gpg')
os.system('sudo apt-get update')
os.system('sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin')
