#/usr/bin/python3

import os
import subprocess
import time

def hadoopConfig():

	def hadoop_install():

		e = subprocess.getstatusoutput("rpm -q hadoop")
		if e[0] != 0:
			print("\nHadoop Is Not Install\n\n")
			time.sleep(1)
			print("Wait A Min Hadoop is Configuring")
			x = subprocess.getstatusoutput("pip3 install gdown")
			if x[0] != 0:
				y = subprocess.getstatusoutput("pip install gdown")
				if y[0] != 0:
					os.system("yum install gdown")
		
			z = subprocess.getstatusoutput("gdown --id 17UWQNVdBdGlyualwWX4Cc96KyZhD-lxz ")
			q = subprocess.getstatusoutput("gdown --id 1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5 ")
			if z[0] == 0 and q[0] == 0:
				print("Hadoop Dependencies Downloaded Successfully")
			else:
				print("Error While Fetching Data")
			
		else:
			print("Hadoop Is Already Installed")


		

	def NameNode():

		x = input("Enter File Name (Without Extension) : ")	
		os.system("mkdir /{}".format(x))

		#hdfs-site.xml file setup
		os.chdir("/etc/hadoop")
		f=open('hdfs-site.xml','w')
		f.write("<?xml version=\"1.0\"?>\n")
		f.write("<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n")

		f.write("<!-- Put site-specific property overrides in this file. -->\n\n")

		f.write("<configuration>\n")
		f.write("<property>\n")
		f.write("<name>dfs.name.dir</name>\n")
		f.write("<value>/"+x+"</value>\n")
		f.write("</property>\n")
		f.write("</configuration>\n")

		f.close()

		#core-site.xml file setup
		os.chdir("/etc/hadoop")
		f=open('core-site.xml','w')
		f.write("<?xml version=\"1.0\"?>\n")
		f.write("<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n")

		f.write("<!-- Put site-specific property overrides in this file. -->\n\n")

		f.write("<configuration>\n")
		f.write("<property>\n")
		f.write("<name>fs.default.name</name>\n")
		f.write("<value>hdfs://0.0.0.0:9001</value>\n")
		f.write("</property>\n")
		f.write("</configuration>\n")
		
		f.close()

		print("#####Your Name Node Is configured Successfully#######\n")
		time.sleep(1)
		print("Wait Name Node Directory is Formating\n")
		os.system("hadoop namenode -format")
		time.sleep(1)
		print("formatted successfully\n")





	def DataNode():
		
		x = input("Enter File Name (Without Extension) : ")
		y = input("Enter Your IP Address: ")
		os.system("mkdir /{}".format(x))

		#hdfs-site.xml file setup
		os.chdir("/etc/hadoop")
		f=open('hdfs-site.xml','w')
		f.write("<?xml version=\"1.0\"?>\n")
		f.write("<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n")

		f.write("<!-- Put site-specific property overrides in this file. -->\n\n")

		f.write("<configuration>\n")
		f.write("<property>\n")
		f.write("<name>dfs.data.dir</name>\n")
		f.write("<value>/"+x+"</value>\n")
		f.write("</property>\n")
		f.write("</configuration>\n")

		f.close()

		#core-site.xml file setup
		os.chdir("/etc/hadoop")
		f=open('core-site.xml','w')
		f.write("<?xml version=\"1.0\"?>\n")
		f.write("<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n")

		f.write("<!-- Put site-specific property overrides in this file. -->\n\n")

		f.write("<configuration>\n")
		f.write("<property>\n")
		f.write("<name>fs.default.name</name>\n")
		f.write("<value>hdfs://"+y+":9001</value>\n")
		f.write("</property>\n")
		f.write("</configuration>\n")
		
		f.close()
		
		print("#####Your Data Node Is configured Successfully#######\n")



	os.system("clear")
	print("\t--------------------------------------------------------")
	os.system("tput setaf 4")
	print("\t\tWelcome To The Hadoop Menu Driven Program")
	os.system("tput setaf 7")
	print("\t--------------------------------------------------------")


	while(1):

			
		os.system("tput setaf 3")
		print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
________________________________________________________________________
Press 1 To Install hadoop.   |	Press 6  To Stop Name Node.
_____________________________|___________________________________________
Press 2  To Set Name Node.   |	Press 7  To Stop data Node.
_____________________________|___________________________________________
Press 3  To Set data Node.   |	Press 8  To Check Data/Name Node Status.
_____________________________|___________________________________________
Press 4  To Start Name Node. | 	Press 9  To Display Hadoop Admin Report.
_____________________________|___________________________________________
Press 5  To Start data Node. |	press 0 For Exit.
_____________________________|___________________________________________
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
NOTE:- Make Sure That Your System Must Be Connectd To The Internet
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

			""")

		os.system("tput setaf 7")	

		choice = input("Enter Your Choice : ")
		
		if int(choice)==1:
			hadoop_install()
			time.sleep(2)
				
		elif int(choice)==2:
			NameNode()
			time.sleep(2)

		elif int(choice)==3:
			DataNode()
			time.sleep(2)	

		elif int(choice)==4:
			os.system("hadoop-daemon.sh start namenode")
			time.sleep(2)
		
		elif int(choice)==5:
			os.system("hadoop-daemon.sh start datanode")
			time.sleep(2)
		
		elif int(choice)==6:
			os.system("hadoop-daemon.sh stop namenode")
			time.sleep(2)

		elif int(choice)==7:
			os.system("hadoop-daemon.sh stop datanode")
			time.sleep(2)

		elif int(choice)==8:
			os.system("jps")
			time.sleep(2)

		elif int(choice)==9:
			os.system("hadoop dfsadmin -report")
			time.sleep(2)	

		elif int(choice) == 0:
			 exit()
		else:
			print("Invalid Input")

		
