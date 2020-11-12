#/usr/bin/python3

import os
import subprocess  

def webConfig():
	print(" wait for a minute we are configuring web server for you")

	x=subprocess.getstatusoutput(" yum list httpd")
	if x[0]==0:
		os.system("yum install httpd")
		print("httpd is Intalled Successfully")
		os.system("systemctl start httpd")
		print("Your Service is Started")
		   
	else:
		os.chdir("/etc/yum.repos.d")
		directory = input("Enter The Directory Name (eg : xyz.repo) : ")
		f=open(directory,'w')
		f.write("[dvd1]\n")
		f.write("baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream\n")
		f.write("gpgcheck=0\n")
		f.write("[dvd2]\n")
		f.write("baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS\n")
		f.write("gpgcheck=0\n")
		f.close
		print(" yum is configured sucessfuly ! for check go at(/etc/yum.repos.d/")
		os.system("yum repolist")
		os.system("yum install httpd")
		print("httpd Intalled Successfully")
		os.system("systemctl start httpd")
		print("Your Service Is Started Now")

	def cp_file():           
		os.chdir("/var/www/html")
		y=subprocess.getstatusoutput("pwd")
		print("""\t\t\tyour current directory is : {} 
			\tPut Your Website File in this location (eg index.html)""".format(y[1]))
	 
		print("\n")	

		print("""\t\t\tpress 1 To copy file from local computer
			\tpress 2 to copy file from a website
			\tpress 3 To open a new file\n""")

		r=input("Enter You Choice Here : ")
	     
		if int(r)==1:
			print("Enter Your Source Path")
			s1=input()
	      
			print("Enter Your Destination Path")
			s2=input()

			m = subprocess.getstatusoutput("cp {} {}".format(s1,s2))        
	      
			if m[0]==0:
				print("copied ")
			else:
				print("Failed To Copying File From Your Source")
		
		elif int(r)==2:
			print("Enter your Website To Download File")
			a1=input()                
	     		
			os.system("wget https:// {}".format(a1))

		elif int(r)==3:
			r1=input(" Enter Your File Name: ")
			os.system("gedit {}".format(r1)) 

		else:
			print("you didnt copy any file :To configure web server you should have to have web code file")

		return print("Your Website Should Have This Path https://your_public_ip/code_file_name \n eg; https://172.0.02.15/new.html")


	c=1
	while int(c)==1: 
	   
		cp_file()
		c=input("To Copy/ Create More File Enter 1: Else Enter Any Number Excluding 1 ")
	    
