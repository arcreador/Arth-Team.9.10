#/usr/bin/python3

import os
import time
import subprocess


def dockerConfig():
	
	

	def dockerYum():
		x = subprocess.getstatusoutput("rpm -q docker-ce")		
		if x[0] == 0:
			print("###Docker is Already Configure In Your System###\n")
			time.sleep(2)
		else:
			print("****Wait a minute We Configuring Docker For You****\n")	
			time.sleep(2)
		
			os.chdir("/etc/yum.repos.d")
			directory = input("Enter The Repository Name (eg : xyz.repo) : ")
			os.system("touch {}".format(directory))
			f=open(directory,'w')
			f.write("[docker321]\n")
			f.write("baseurl=https:///download.docker.com/linux/centos/7/x86_64/stable\n")
			f.write("gpgcheck=0\n")
			f.close()
			
			os.system("yum repolist")
			print("\n\n****Yum is Successfully Configure For Docker ****\n")	
			time.sleep(2)
			print("\nPress 2 For Instllation Of Docker\n")


	def docker(y,start):
		
			if y[0] == 0:
				print("\nDocker {} Successfully....!\n".format(start))
				time.sleep(4)
			else:
				print("\nProcess Failed Check First Yum Is Configured For Docker Or Not\n")
				time.sleep(4)
		
			


	os.system("clear")
	print("\t\t----------------------------------------------------------")
	os.system("tput setaf 4")
	print("\t\t\tWelcome To The Docker Menu Driven Program")
	os.system("tput setaf 7")
	print("\t\t----------------------------------------------------------")


	while(1):
		os.system("tput setaf 3")
		print("""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
____________________________________________________________________________________
Press 1 To Configure Yum For Docker  |	Press 7 To Display All Available Images.. 
_____________________________________|______________________________________________
Press 2 To Install Docker.           |	Press 8 To Luanch Dokcer Container. 
_____________________________________|_______________________________________________
Press 3 To Start The Dokcer Services.|	Press 9 To Display All Running Containers. 
_____________________________________|_______________________________________________
Press 4 To Stop The Dokcer Services. |	Press 10 To Display All stoped Containers. 
_____________________________________|_______________________________________________
Press 5 Check Is Dokcer running.     |	Press 11 To Attach The Containers. 
_____________________________________|_______________________________________________
Press 6 To Pull The Images of OS.    |	Press 12 To Deleting Containers.
_____________________________________|_______________________________________________
press 0 For Terminate Program 	     |	Press 13 To Deleting images.	
_____________________________________|________________________________________________
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
NOTE :- 1.Type 'exit' or Ctr+Q For Exiting Docker Container.
	2.Press Q or Ctr+Q to Exit from Local System.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		
			""")

		os.system("tput setaf 7")

		choice = input("Enter Your Choice : ")
			
		if int(choice) == 1:
			dockerYum()

		elif int(choice) == 2:
			print("\nDocker Is Installing Wait....\n")
			y = subprocess.getstatusoutput("yum install docker-ce --nobest")
			#os.system("dnf clean package")
			status = "installed"
			docker(y,status)
			

		elif int(choice) == 3:
			y = subprocess.getstatusoutput("systemctl start docker")
			status = "Is started"
			docker(y,status)

		elif int(choice) == 4:
			y = subprocess.getstatusoutput("systemctl stop docker")
			status = "Is Stop"
			docker(y,status)

		elif int(choice) == 5:
			os.system("systemctl status docker")
			y = subprocess.getstatusoutput("systemctl status docker")
			status = "Is running"
			os.system("clear")
			os.system("python3 dockers.py")
			docker(y,status)

		elif int(choice) == 6:
			name = input("Enter Image Name : ")
			version = input("Enter Version Of Image : ")
			print("\nDocker Image Is Pulling Wait a minute ...\n")
			y = subprocess.getstatusoutput("docker pull {}:{}".format(name,version))
			status = "Image {}:{} Is Pulled".format(name,version)
			docker(y,status)

		elif int(choice) == 7:
			os.system("docker images")
			time.sleep(5)	

		elif int(choice) == 8:
			cName = input("Enter Name Of Container As Per Your Choice : ")
			name = input("Enter Image Name : ")
			version = input("Enter Version Of Image : ")
			print("\nWait Container is Launching.....")
			y = subprocess.getstatusoutput("docker run -i -d --name {} {}:{}".format(cName,name,version))
			status = "Container {} Is Launch".format(cName)
			docker(y,status)
			exit()
		
		elif int(choice) == 9:
			os.system("docker ps")
			time.sleep(5)

		elif int(choice) == 10:
			os.system("docker ps -a")
			time.sleep(5)

		elif int(choice) == 11:
			name = input("Enter The Container ID/Name To attach : ")
			y = subprocess.getstatusoutput("docker attach {}".format(name))
			status = "Container {} Is Attached".format(name)
			docker(y,status)
			exit()

		elif int(choice) == 12:
			ch = int(input("For Deleting Specific Container Press 1 or For Deleting All Press 2 :  "))	
			if ch == 1:
				name = input("Enter Container Name/ID : ")
				print("\nContainer Is Deleting Wait............")
				y = subprocess.getstatusoutput("docker rm -f {}".format(name))
				status = "Container {} Is Deleted".format(name)
				docker(y,status)
			else:
				print("\nContainer Is Deleting Wait............")		
				y = subprocess.getstatusoutput("docker rm -f `docker ps -a -q`")
				status = "All Container Are Deleted"
				docker(y,status)

		elif int(choice) == 13:
			ch = int(input("For Deleting Specific Image Press 1 or For Deleting All Images Press 2 :  "))	
			if ch == 1:
				name = input("Enter Image Name : ")
				ids = input("Enter Image Version : ")
				print("\nImage Is Deleting Wait............")
				y = subprocess.getstatusoutput("docker rmi  {}:{}".format(name,ids))
				status = "Image {}:{} Is Deleted".format(name,ids)
				docker(y,status)
			else:
				print("\nImages Is Deleting Wait............")		
				y = subprocess.getstatusoutput("docker rmi  `docker images -a -q`")
				status = "All Images Are Deleted"
				docker(y,status)

		elif int(choice) == 0:
			exit()

		else:
			print("Invalid Input")

			
