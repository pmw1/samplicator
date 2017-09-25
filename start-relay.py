#!/usr/bin/python3

import sys
import random
import os

user=os.getlogin()
cmd="samplicate "
cmd+="-d1 "
cmd+="-s0.0.0.0 "

print ("Starting Relay Server / UDP")


#####################################################################################
########################  PARSE ARGUEMENTS INTO VARIABLES ###########################
if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('--listen', '-l', help="port to receive on")
	parser.add_argument('--dest1', '-1', help="IP Address for Destination 1")
	parser.add_argument('--dest2', '-2', help="IP Address for Destination 2")
	parser.add_argument('--dest3', '-3', help="IP Address for Destination 3")
	parser.add_argument('--dest4', '-4', help="IP Address for Destination 4")
	parser.add_argument('--dest5', '-5', help="IP Address for Destination 5")
	parser.add_argument('--dest6', '-6', help="IP Address for Destination 6")
	parser.add_argument('--dest7', '-7', help="IP Address for Destination 7")
	parser.add_argument('--dest8', '-8', help="IP Address for Destination 1")
	parser.add_argument('--dest9', '-9', help="IP Address for Destination 1")
	parser.add_argument('--port1', '-p1', help="Port Number for Destination 1")
	parser.add_argument('--port2', '-p2', help="Port Number for Destination 2")
	parser.add_argument('--port3', '-p3', help="Port Number for Destination 3")
	parser.add_argument('--port4', '-p4', help="Port Number for Destination 4")
	parser.add_argument('--port5', '-p5', help="Port Number for Destination 5")
	parser.add_argument('--port6', '-p6', help="Port Number for Destination 6")
	parser.add_argument('--port7', '-p7', help="Port Number for Destination 7")
	parser.add_argument('--port8', '-p8', help="Port Number for Destination 8")
	parser.add_argument('--port9', '-p9', help="Port Number for Destination 9")
	parser.add_argument('--force', '-f', help="Force kill other direct-send container before starting")
	parser.add_argument('--destroy', '-d', help="Destroy direct-send container")

	# Replicate above line to add more optional input arguments
	
	args = parser.parse_args()

	destroy=args.destroy
	force=args.force


	if args.listen is not None:
		print("listening for UDP data on port: " + args.listen)
		cmd+=("-p" + args.listen + " ")
		port=args.listen
	else:
		print("Incoming (listening) port must be defined")
		quit()

	if args.dest1 is not None and args.port1 is not None:
		print ("Setting Destination 1: " + args.dest1 + "/" + args.port1)
		cmd+=args.dest1 + "/" + args.port1 + " "
	else:
		print("Destination 1 (IP AND Port) must be defined")
		quit()

	if args.dest2 is not None and args.port2 is not None:
		print ("Setting Destination 2: " + args.dest2 + "/" + args.port2)
		cmd+=args.dest2 + "/" + args.port2 + " "

	if args.dest3 is not None and args.port3 is not None:
		print ("Setting Destination 3: " + args.dest3 + "/" + args.port3)
		cmd+=args.dest3 + "/" + args.port3 + " "

	if args.dest4 is not None and args.port4 is not None:
		print ("Setting Destination 4: " + args.dest4 + "/" + args.port4)
		cmd+=args.dest4 + "/" + args.port4 + " "

	if args.dest5 is not None and args.port5 is not None:
		print ("Setting Destination 5: " + args.dest5 + "/" + args.port5)
		cmd+=args.dest5 + "/" + args.port5 + " "

	if args.dest6 is not None and args.port6 is not None:
		print ("Setting Destination 6: " + args.dest6 + "/" + args.port6)
		cmd+=args.dest6 + "/" + args.port6 + " "

	if args.dest7 is not None and args.port7 is not None:
		print ("Setting Destination 7: " + args.dest7 + "/" + args.port7)
		cmd+=args.dest7 + "/" + args.port7 + " "

	if args.dest8 is not None and args.port8 is not None:
		print ("Setting Destination 8: " + args.dest8 + "/" + args.port8)
		cmd+=args.dest8 + "/" + args.port8 + " "

	if args.dest9 is not None and args.port9 is not None:
		print ("Setting Destination 9: " + args.dest9 + "/" + args.port9)
		cmd+=args.dest9 + "/" + args.port9 + " "



print("Execute Command: " + cmd)

#####################################################################################
########################  END PARSE ARGUEMENTS INTO VARIABLES #######################








#####################################################################################
########################  BUILD SAMPLICATOR DOCKER FOR RELAY  #######################
def buildRelayDocker():
	print('*** building relay docker ***')

	import subprocess
	import stat
	## open file for writing
	start_docker_file = open("/home/" + user + "/apps/samplicator/start-docker.sh", "wb")
	start_docker_file.write(bytes("#!/bin/bash\n", 'UTF-8'))
	start_docker_file.write(bytes("sudo docker rm -f relay\n", 'UTF-8'))
	start_docker_file.write(bytes("sudo docker run ", 'UTF-8'))
	start_docker_file.write(bytes("--network=\"docker-network\" ", 'UTF-8'))
	start_docker_file.write(bytes("--ip=\"10.0.10.2\" ", 'UTF-8'))
	start_docker_file.write(bytes("--name \"relay\" ", 'UTF-8'))
	start_docker_file.write(bytes("-v /home/" + user + "/apps/samplicator/hostfiles:/hostfiles ", 'UTF-8'))
	start_docker_file.write(bytes("-p{}:{}/udp ".format(port, port), 'UTF-8'))
	start_docker_file.write(bytes("--privileged -i -t -d ", 'UTF-8'))
	start_docker_file.write(bytes("--entrypoint=\"/hostfiles/samplicator-start.sh\" " , 'UTF-8'))
	##start_docker_file.write(bytes("--entrypoint=\"/bin/bash\" " , 'UTF-8'))
	start_docker_file.write(bytes("pmw1/samplicator", 'UTF-8'))

	start_docker_file.close()

	os.chmod("/home/" + user + "/apps/samplicator/start-docker.sh", stat.S_IXOTH)
	proc = subprocess.Popen("sudo /home/" + user + "/apps/samplicator/start-docker.sh", shell=True)


###################### END BUILD SAMPLICATOR DOCKER FOR RELAY  #######################
######################################################################################









#####################################################################################
########################  BUILD SAMPLICATOR ENTRYPOINT    ###########################
def buildRelayEntrypoint():
	print('*** building entrypoint ***')

	import subprocess
	import stat
	## open file for writing
	entrypoint_file = open("/home/" + user + "/apps/samplicator/hostfiles/samplicator-start.sh", "wb")
	entrypoint_file.write(bytes("#!/bin/bash\n", 'UTF-8'))
	entrypoint_file.write(bytes(cmd, 'UTF-8'))


	entrypoint_file.close()

	os.chmod("/home/" + user + "/apps/samplicator/hostfiles/samplicator-start.sh", stat.S_IXOTH)
	
	## no need to execute entrypoint on host
	##proc = subprocess.Popen('sudo start-docker.sh', shell=True)


###################### END BUILD SAMPLICATOR ENTRYPOINT  #############################
######################################################################################











def checkForceDestroy():
	if destroy=='1':
		print("RELAY INSTANCE DESTROYED")
		bashCommand="sudo docker rm -f relay"
		os.system(bashCommand)
		quit()

	if force=='1':
		print("FORCING START by KILLING PREVIOUS CONTAINED")
		bashCommand="sudo docker rm -f relay"
		os.system(bashCommand)



checkForceDestroy();


buildRelayEntrypoint();


buildRelayDocker();










