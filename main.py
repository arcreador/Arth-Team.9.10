#/usr/bin/python3

import os
import time
import sys
import dockers
import lvm
import hadoop
import webserver
import awss

	
os.system("clear")
print("\t\t----------------------------------------------------------")
os.system("tput setaf 4")
print("\t\tWelcome To The Arth Group 9 Team 10 Menu Driven Program")
os.system("tput setaf 7")
print("\t\t----------------------------------------------------------")


while(1):

	print("\n\n\t\t----------------------------------------------------------")	
	os.system("tput setaf 3")
	print("""
		\tPress 1 Docker Configration.
		\t______________________________________
		\tPress 2 For Logical Volume Management 
		\t______________________________________
		\tPress 3 For Hadoop Configration. 
		\t______________________________________
		\tPress 4 To Configure Web Server. 
		\t______________________________________
		\tPress 5 AWS Configration.
		\t______________________________________
		\tpress 0 For Exit.		
		""")

	os.system("tput setaf 7")
		
	print("\t\t----------------------------------------------------------")	

	choice = input("Enter Your Choice : ")
	if int(choice)==1:
		dockers.dockerConfig()

	elif int(choice)==2:
		lvm.lvManage()

	elif int(choice)==3:
		hadoop.hadoopConfig()

	elif int(choice)==4:
		webserver.webConfig()

	elif int(choice)== 5:
		awss.awsFunction()		

	elif int(choice) == 0:
		print("""\t\t\t****************************************
				Program Is Terminated 
			*****************Thank You**************\n""")		
		sys.exit()
		
	else:
		print("Invalid Input")



		
