#/bin/bash
echo "running samplicator docker: 10.0.10.11"

sudo docker kill samplicator
sudo docker rm -f samplicator



sudo docker run \
	-i -t \
	-v $HOME/apps/samplicator/hostfiles/:/hostfiles \
	-p 3001:3001/udp \
	--name="samplicator" \
	--network="docker-network" \
	--ip="10.0.10.2" \
	pmw1/samplicator

samplicateCmd="samplicate"
