#!/bin/bash
sudo docker rm -f relay
sudo docker run --network="docker-network" --ip="10.0.10.2" --name "relay" -v /home/ubuntu/apps/samplicator/hostfiles:/hostfiles -p3001:3001/udp --privileged -i -t -d --entrypoint="/hostfiles/samplicator-start.sh" pmw1/samplicator