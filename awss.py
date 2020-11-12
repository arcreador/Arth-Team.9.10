import os
import subprocess
import time

def awsFunction():
	def Ec2():
		print("\n \t \t\t\twelcome to EC2 menu\n")
		print("""\t\t\t\t1.Enter 1 to know state of your of EC2 Instances
				2.Enter 2 to launch a new ec2 instance 
				3.Enter 3 to start a instance 
				4.Enter 4 to  stop a instance
				5.Enter 5 to terminate an instance""")
		x=input("\n Enter your choice:")
		if int (x)==1:
			os.system("aws ec2 describe-instances")
		elif int(x)==2:
			print("\n\tyou should have keypair value to run a instance")

			im=input("\nEnter your image id:")

			cnt=input("\nEnter your count:")

			key=input("\nEnter your key name:")

			instyp=input("\nEnter your instance type:")

			subnet = input("\nEnter Your Subnet ID : ")

			print("\n\t\t your ec2 is launching")

			os.system("aws ec2 run-instances  --image-id {} --count {}  --subnet-id {} --instance-type {} --key-name {} ".format(im,cnt,subnet,instyp,key,))
			 
		elif int(x)==3:
			print("\nEnter Your instance id:")
			ids=input()
			os.system("aws ec2 start-instances --instance-id {}".format(ids))
			
		elif int(x)==4:
			print("\nEnter Your instance id:")
			ids=input()
			os.system("aws ec2 stop-instances --instance-id {}".format(ids))
		     
		elif int(x)==5:
			print("\nEnter Your instance id:")
			ids=input()
			os.system("aws ec2 terminate-instances --instance-id {}".format(ids))
			
		else: 
			print("\n \tInvalid input")
			x=input("Do u want to go back to AWS Menu.Press 1 to GO Back To aws menu else press any number:")
			if int (x)==1:
				aws()
		


	def Key_pair():
		print("\n \t \t\t\twelcome to KEY menu")
		print ("\n ")
		print("""\t\t\t\t1.Enter 1 to  create key pair
				2.Enter 2 delete a new key pair
				3.Enter 3 to know about created key pair""")
		x=input("\n Enter your choice:")
				
		if int (x)==1:
			ids=input("\nEnter your Keyname:")
			kfile=("\n enter a file name with extension :name should be .pem extention")
			os.system("aws ec2 create-key-pair --key-name {} >{}".format(ids,kfile))
			print("\n\t key is saved in mykey.pem file")
		elif int (x)==2:
			ids=input("\nEnter your Keyname:")
			os.system("aws ec2 delete-key-pair --key-name {}".format(ids)) 
				
		elif int (x)==3:
			os.system("aws ec2 describe-key-pairs --key-name ")
		
		else:
			print("\n \tInvalid input")
			x=input("Do u want to go back to AWS Menu.Press 1 to GO Back To aws menu else press any number:")
			if int (x)==1:
				aws() 
			
	def Ebs():
		print("\n \t \t\t\twelcome to Ebs menu")
		print ("\n ")
		print("""\t\t\t\t1.Enter 1 to know about your created Ebs volume 
				2.Enter 2 create a new volume 
				3.Enter 3 to delete a volume
				4.Enter 4 to attach the volume to ec2
				5.Enter 5 to detach volume from ec2 instance""")

		x=input("\n Enter your choice:")

		if int (x)==1:
			os.system("aws ec2 describe-volumes")
		     
		elif int (x)==2:
			ids=input("\nEnter your volume tpye:")
			size=input("\nEnter your volume size:")
			avzone=input("\nEnter availablity zone where do u want to create volume:")
			os.system("aws ec2 create-volume --volume-type {} --size {} --availability-zone {}".format(ids,size,avzone))
				
		elif int (x)==3:
			ids=input("\nEnter your volume id to be deleted:")
			os.system("aws ec2 delete-volume --volume-id {}".format(ids))
				
		elif int (x)==4:
			ids=input("\nEnter your volume id :")
			inid=input("\nEnter your instance id:")
			dev=input("\nEnter device name:")
			os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device {}".format(ids,inid,dev)) 
				
		elif int (x)==5:
			ids=input("\nEnter your volume id:")
			os.system("aws ec2 detach-volume --volume-id {}".format(ids))
				
		else:
			print("\n \tInvalid input")
			x=input("Do u want to go back to AWS Menu.Press 1 to GO Back To aws menu else press any number:")
			if int (x)==1:
				aws() 
		
	def s3():
		print("\n \t \t\t\twelcome to S3 menu")
		print("\n \t \t\t\tNote:All bucket name should start with s3:// like s3://bucket")	
		print("\n ")

		print("""\t\t\t\t1.Enter 1 Create a bucket
				2.Enter 2 list bucket object
				3.Enter 3 to delete delete bucket
				4.Enter to upload a object
				5.Enter 5 to delete a object
			""")

		x=input("\n Enter your choice:")

		if int(x)==1:
			name=input("\nEnter bucket name to be create:")
			os.system("aws s3 mb {}".format(name))
			   
		elif int(x)==2:
			name=input("\nEnter bucket name to be listed:")
			os.system("aws s3 ls {}".format(name))
			   
		elif int(x)==3:
			name=input("\nEnter bucket name to be deleted:")
			os.system("aws s3 rb {} --force".format(name))
			   
			    	
		elif int(x)==4:
			name=input("\nEnter bucket name:")
			path=input("\nEnter object path:")
			os.system("aws s3 cp {} {}".format(path,name))
			
		elif int(x)==5:
			path=input("\nEnter object path:")
			os.system("aws s3 rm {}".format(path))
				
		else:
			print("\n \tInvalid input")
			x=input("Do u want to go back to AWS Menu.Press 1 to GO Back To aws menu else press any number:")
			if int (x)==1:
				aws()
			    
			
	def sg():
		print("\n \t \t\t\twelcome to S3 menu")
		print ("\n ")
		print("""\t\t\t\t1.Enter 1 know about created security group
				2.Enter 2 to create security group
				3.Enter 3 to delete a security group
			""")
		
		x=input("\n Enter your choice:")

		if int(x)==1:
			os.system("aws ec2 describe-security-groups")
		elif int(x)==2:
			name=input("\nEnter group name to be created:")
			name1=input("\nEnter group description to be listed:")
			os.system("aws ec2 create-security-group --group-name {} --description {} ".format(name,name1))
			  
		elif int(x)==3:
			name=input("\nEnter security group id to be deleted:")
			os.system("aws ec2 delete-security-group --group-id {} ".format(name)) 
				
		else:
			print("\n \tInvalid input")
			x=input("Do u want to go back to AWS Menu.Press 1 to GO Back To aws menu else press any number:")
			if int (x)==1:
				aws()
			      

			     
	os.system("clear")
	f=subprocess.getstatusoutput("aws")
	s=f[1]
	s=s.find("command not found")
	s=-1
	if s!=-1:
		print("you don't have aws cli either software downloaded or installed")
	else:
		print("\n \t \t\t\twelcome to AWS menu")
		print ("\n ")
		print("""\t\t\t\t1.Enter 1 to know available  option of EC2 Instances
				2.Enter 2 to know available option of KEY PAIR
				3.Enter 3 to konw availble option of EBS
				4.Enter 4 to know available option of S3
				5.Enter 5 to know available option of security group
			""")
		
		t=input("\nEnter Your Choice:")
		s=1
		while int(s)==1:
			if int (t)==1:
				Ec2()
				break
			elif int(t)==2:
				Key_pair()
				break
			elif int(t)==3:
				Ebs()
				break
			elif int(t)==4:
				s3()
				break
			elif int(t)==5:
				sg()
				break
			else:
				print("\ninvaild input !! please enter valid input or press 9 to quit")
				t=input("\nEnter your valid choice:")
				if int(t)==9:
					break;    




		   

