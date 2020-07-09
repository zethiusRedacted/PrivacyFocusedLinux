#!/bin/python3
#zethius 'skengman' redacted presents the 'Privacy Focused Linux'
#this program only runs on ubuntu-minimal

#importing OS for system commands
import os
#importing time for organisation purposes
import time
#displaying time for syslog
from datetime import datetime as dt
	
def aClean():
	 
	 #autocleans and autoremoves files
	 print("Removing...")
	 os.system("sudo apt-get -y autoremove")
	 time.sleep(1)
	 
	 print("\nCleaning...")
	 os.system("sudo apt-get autoclean && sudo apt-get clean")
	 time.sleep(1)
	 
	 print("-"*50)
	 print("YOU HAVE BEEN...PRIVATISED ( ͡° ͜ʖ ͡°)")
	 print("-"*50)
	 
	 print("Press Enter to reboot...")
	 input()
	 os.system("sudo reboot")
	 
	 return()
	
def privInstall():
	
	#this function installs privacy enhancing tools to your distro
	
	#mat (metadata anonymisation tool) deletes metadata from files
	print("""Metadata Anonymisation Tool (i.e., MAT) removes metadata from images, documents and other types of files.""")
	os.system("sudo apt-get install -y mat")
	time.sleep(1)
	
	#secure-delete allows you to securely delete files
	print("""\nSecure-Delete (srm) allows you to securely delete files which disables forensic teams to recover it.""")
	os.system("sudo apt-get install -y secure-delete")
	time.sleep(1)
	
	#UFW or uncomplicated fire wall
	print("""\nUncomplicated Firewall blocks all shady traffic in or out of your computer.""")
	os.system("sudo apt-get install -y ufw")
	os.system("sudo ufw enable")
	time.sleep(1)
	
	#HTOP allows you to moniter the ongoing processes
	print("""\nHTOP allows you to monitor all the ongoing processes on your computer.""")
	os.system("sudo apt-get install -y htop")
	time.sleep(1)
	
	#locate helps you locate packages/documents with a mere command
	print("""\nLocate allows you to search for packages, software or documents with one mere command.""")
	os.system("sudo apt-get install -y locate")
	time.sleep(1)
	
	#MacChanger allows you to change/spoof your MAC address
	print("""\nMAC Changer allows you to change or spoof your MAC address.""")
	os.system("sudo apt-get install -y macchanger")
	time.sleep(1)
	
	#Nautilus Wipe allows you to delete files securely in a GUI interface
	print("""\nNautilus Wipe (nautilus-wipe) allows you to securely delete files in a GUI interface to protect them from recovering forensic teams.""")
	os.system("sudo apt-get install -y nautilus-wipe")
	time.sleep(1)
	
	#ClamAV and #ClamTK helps you search for and eliminate virus/ransomware/malware
	print("""\nClam Antivirus (clamav) and ClamTK (GUI ClamAV) enables you to scan your computer and eliminate viruses/malware/ransomeware.""")
	os.system("sudo apt-get install -y clamav && sudo apt-get install -y clamtk")
	time.sleep(1)
	
	#KeePassXC is an oper-source, offline, and encrypted password manager
	print("""\nKeePassXC is an open-source, offline and encrypted password manager which allows you to save password securely.""")
	os.system("sudo apt-get install -y keepassxc")
	time.sleep(1)
	
	#GTKHash is a GUI hash checker
	print("""\nGTK Hash allows you to check hash fingerprinting of a file.""")
	os.system("sudo apt-get install -y gtkhash")
	time.sleep(1)
	
	print("-"*50)
	
	aClean()
	
	return()
	
def classicLin():

	print("Disabling Ubuntu Dock...\n")
	os.system("sudo apt-get purge -y gnome-shell-extension-ubuntu-dock")
	time.sleep(1)
	
	privInstall()
	
	return()

#minmise information about the user reaching canonical
#purging snap and setting up an alternative i.e., flatpak
def deSnap():

	print("-"*50)
	print("DESNAPING AND MAKING MORE PRIVATE")
	print("-"*50)
	print("""Important Information: Apport reports all user activity to Canonical by default. Even if you disable reporting, Ubuntu still are aware of the number of users they have. Disabling Apport takes care of that.""")
	print("-"*50)
	
	#snap-store gtk-common-themes gnome-3-34-1804 core18 snapd purge
	#disabling apport which reports user information to canonical
	print("Disabling Apport...\n")
	time.sleep(1)
	os.system("sudo sed -i 's/enabled=1/enabled=0/g' /etc/default/apport")
	print("...")
	print("Done!\n")
	
	#most people tend to distrust Snap and hence its removal
	print("Purging Snap completely...\n")
	time.sleep(1)
	#removing the snap-store completely
	os.system("sudo apt-get purge -y snapd")
	print("...")
	print("Done!\n")
	
	#as a substitution for a package manager, flatpak will be installed
	print("Installing Flatpak...\n")
	time.sleep(1)
	os.system("sudo apt-get install -y flatpak")
	os.system("flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo")
	os.system("sudo apt-get install -y gnome-software-plugin-flatpak")
	
	#install flatpak plugin installs snapd again so purging it again
	os.system("sudo apt-get purge -y gnome-software-plugin-snap")
	os.system("sudo apt-get purge -y snapd")
	print("...")
	print("Done!\n")
	
	time.sleep(1)
	#automatic updates are also a security risk
	print("Disabling automatic updates...\n")
	os.system("sudo apt-get purge -y update-notifier")
	
	#ubuntu-dock is not a privacy concern and hence a choice
	time.sleep(1)
	print("""\nFor a more classic GNOME experience, would you like to delete the Ubuntu Dock? (Y/N)""")
	classicLin_ques = input()
	classicLin_ques.lower()
	print()
	
	if classicLin_ques == "y" or classicLin_ques == "yes":
		classicLin()
	elif classicLin_ques == "n" or classicLin_ques == "no":
		privInstall()
	else:
		classicLin()
	
	
	return()

def start_prog():
	#introduction to the program
	print("-"*50)
	print("PRIVACY FOCUSED LINUX")
	print(dt.now())
	print("-"*50)

	#running updates and upgrades before the program begins
	print("Updating")
	print("-"*50)
	os.system("sudo apt-get -y update")
	time.sleep(1)

	#running a full-upgrade to install upgrades and delete old packages
	print("-"*50)
	print("Upgrading")
	print("-"*50)
	os.system("sudo apt-get -y full-upgrade")
	time.sleep(1)
	
	#running the deSnapping program
	deSnap()
	
	return()
	
#asking the user if they are using ubuntu-minimal
print("Are you running Ubuntu-Minimal? (Y/N)")
ques = input()
ques.lower()

if ques == "yes" or ques == "y":
	#starting the program if they are
	start_prog()
elif ques == "no" or ques == "n":
	#asking them to install it if they are not
	time.sleep(1)
	print("\nUnfortunately, this program was designed for Ubuntu-Minimal.")
	print("Please re-install Ubuntu for maximum privacy.\n")
	input()
else:
	input("\n")
