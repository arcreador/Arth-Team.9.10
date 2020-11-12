import os
import time
import subprocess


def lvManage():
	def maind():
		os.system("clear")
		print("\t\t\t-------------------------------------------")
		os.system("tput setaf 4")
		print("\t\t\tWelcome To The Arth Menu Driven Program")
		os.system("tput setaf 7")
		print("\t\t\t--------------------------------------------")


	

		print("\n\n\t\t\t--------------------------------------------")	
		os.system("tput setaf 3")
		print("""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
_________________________________________________________________________________
Press 1 To See Available Disk For LVM.	  |press  0 For Exit.
__________________________________________|______________________________________
Press 2 Create Physical Volume.		  |Press 7 Format Created partition.  
__________________________________________|______________________________________
Press 3 Display Physical Volume.	  |Press 8 Mount The partiton On Folder.
__________________________________________|______________________________________
Press 4 Creating Volume Group.		  |Press 9 Extend The volume group.
__________________________________________|______________________________________
Press 5 Display List Of Volume Group.	  |Press 10 Extend The Logical volume.
__________________________________________|______________________________________
Press 6 Create partition Of volume Group. |	
__________________________________________|______________________________________
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
NOTE : Make Sure You Attachted New Hard Disk While Runnig This Function On Your System 				
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")

		os.system("tput setaf 7")
		
		print("\t\t\t----------------------------------------------")	

		choice = input("Enter Your Choice : ")

		if int(choice) == 1:
			y = subprocess.getstatusoutput("fdisk -l | less")
			print("\n")			
			print(y[1])
			time.sleep(5)
		elif int(choice) == 2:
			DL = input("Enter Disk Location : ")
			x = subprocess.getstatusoutput("pvcreate {}".format(DL))
			if x[0] == 0:
				print("\n{}\n".format(x[1]))
			else:
				print("\n{}\n".format(x[1]))			
			time.sleep(2)

		elif int(choice) == 3:
			os.system("pvdisplay")
			time.sleep(5)
			os.system("clear")

		elif int(choice) == 4:
			vgName = input("Enter Volume Group Name (it must be unique in local system) : ")
			DLoc = input("Location of Physical volume : ")
			x = subprocess.getstatusoutput("vgcreate {} {}".format(vgName,DLoc))
			

		elif int(choice) == 5:
			os.system("vgdisplay | less")

		elif int(choice) == 6:
			size =  input("Enter the Size of Logical Partition like (+1G,+1M..) : ")
			lvname = input("Enter the Logical Volume Name : ")
			vgN =  input("Enter Volume Group name : ")
			os.system("lvcreate --size {} --name {} {}".format(size,lvname,vgN))

		elif int(choice)== 7:
			vg = input("Enter The Volume Group Name : ")
			lv = input("Enter The Logical Volume Name : ")
			os.system("mkfs /dev/{}/{}".format(vg,lv))

		elif int(choice) == 8:
			folder = input("Enter Folder Name : ")
			os.system("mkdir /{}".format(folder))
			vg = input("Enter The Name of Volume Group : ")
			lv = input("Enter The Name of Logical Volume : ")
			os.system("mount /dev/{}/{}  /{} ".format(vg,lv,folder))

		elif int(choice) == 9:
			vg = input("Enter The Name of Volume Group : ")
			evg = input("Enter The New Disk Path like (/dev/xyz) : ")
			os.system("vgextend {} {}".format(vg,evg))
			time.sleep(5)

		elif int(choice) == 10:
			elv = input("Enter The Size like(+1G,+1M...) : ")
			vg = input("Enter The Volume Group Name : ")
			lv = input("Enter The Logical Volume Name : ")
			os.system("Extend --size {} /dev/{}/{} ".format(elv,vg,lv))

		elif int(choice) == 0 :
			return exit()
				
			
		else:
			print("Invalid output")

	os.system("tput setaf 4")
	print("""\t\t\t1.Press 1 for Start 
			2.Press Any Number For Go Back In Previous Menu""")
	
	os.system("tput setaf 7")	
	ch = int(input(": "))
	while ch == 1:
		maind()
		
