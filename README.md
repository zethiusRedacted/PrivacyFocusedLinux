# PrivacyFocusedLinux

An Ubuntu-Minimal script which keeps privacy and security in mind. Fully open-sourced and well-explained.
This script was created by Zethius 'Skengman' Redacted using Python3. It automates the rather long and tedious process of enhancing privacy in this well used distribution by newcommers and veterans alike who care about their privacy and security online.
Ubuntu is a great start for a newcommer to Linux and a script which makes the process of privatising faster, more efficient and easier as it may seem rather complicated to a newcommer.

This script performs the following actions:
- Disables Ubuntu reporting back to Canonical by disabling Apport.
- Disables and purges Snap, Snap-Store and Snap packages completely.
- Installs Flatpak instead of Snap.
- Disables automatic updates which can be a security risk.
- Users are given a choice to keep or remove the Ubuntu-Dock for a cleaner and a more classic GNOME experience.

The following privacy enhancing packages are installed:
- MAT2 (metadata anonymisation tool) helps you remove metadata from images and documents alike from either a GUI interface or a command-line interface.
- SRM (secure-delete) allows you to securely delete files using a command-line interface. This prevents forensic teams to recover your deleted data by using the command (srm [File] -rzv for directories and srm [File] -zv for files). In addition, shred (which is pre-installed can be used too). The command shred [xyz] -fzvu can be used to do so.
- UFW (uncomplicated firewall) is an uncomplicated firewall which monitors all the incoming and the outgoing traffic from your computer. 
- HTOP allows you monitor all the ongoing processes on your machine.
- Locate is a simple linux tool which helps you look for files using a command-line interface with relitive ease. (locate [file])
- MacChanger changes your machine's MAC address and hence increases anonymity.
- Nautilus Wipe is a GUI tool for wiping a file which yet again prevents forensic teams to recover your precious deleted data.
- ClamAV and ClamTK (clam antivirus) are anti-virus tools which scan your directories looking for potential harmful processes. ClamTK is a GUI version of it.
- KeePassXC is an open source, encrypted and offline password manager.
- GTKHash enables you to check the hash fingerprinting of files.

In addition to these tools, I would recommend installing some others.
- Signal Desktop for an open source messaging procedure which is end to end encrypted.
- BleachBit for maintenance.

Here is a text version of the scrypt for you to look at:

#!/bin/python3
#zethius 'skengman' redacted presents the 'Privacy Focused Linux'
#this program only runs on ubuntu-minimal

#importing OS for system commands
import os
#importing time for organisation purposes
import time
#displaying time for syslog
from datetime import datetime as dt

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
	
def aClean():
	 
	 #autocleans and autoremoves files
	 print("Removing...")
	 os.system("sudo apt-get autoremove")
	 time.sleep(1)
	 
	 print("\nCleaning...")
	 os.system("sudo apt-get autoclean && sudo apt-get clean")
	 time.sleep(1)
	 
	 print("-"*50)
	 print("YOU HAVE BEEN...PRIVATISED ( ͡° ͜ʖ ͡°)")
	 print("-"*50)
	 
	 input()
	 return()
	
def privInstall():
	
	#this function installs privacy enhancing tools to your distro
	
	#mat (metadata anonymisation tool) deletes metadata from files
	print("""Metadata Anonymisation Tool (i.e., MAT) removes metadata from images, documents and other types of files.""")
	os.system("sudo apt-get install mat")
	time.sleep(1)
	
	#secure-delete allows you to securely delete files
	print("""\nSecure-Delete (srm) allows you to securely delete files which disables forensic teams to recover it.""")
	os.system("sudo apt-get install secure-delete")
	time.sleep(1)
	
	#UFW or uncomplicated fire wall
	print("""\nUncomplicated Firewall blocks all shady traffic in or out of your computer.""")
	os.system("sudo apt-get install ufw")
	os.system("sudo ufw enable")
	time.sleep(1)
	
	#HTOP allows you to moniter the ongoing processes
	print("""\nHTOP allows you to monitor all the ongoing processes on your computer.""")
	os.system("sudo apt-get install htop")
	time.sleep(1)
	
	#locate helps you locate packages/documents with a mere command
	print("""\nLocate allows you to search for packages, software or documents with one mere command.""")
	os.system("sudo apt-get install locate")
	time.sleep(1)
	
	#MacChanger allows you to change/spoof your MAC address
	print("""\nMAC Changer allows you to change or spoof your MAC address.""")
	os.system("sudo apt-get install macchanger")
	time.sleep(1)
	
	#Nautilus Wipe allows you to delete files securely in a GUI interface
	print("""\nNautilus Wipe (nautilus-wipe) allows you to securely delete files in a GUI interface to protect them from recovering forensic teams.""")
	os.system("sudo apt-get install nautilus-wipe")
	time.sleep(1)
	
	#ClamAV and #ClamTK helps you search for and eliminate virus/ransomware/malware
	print("""\nClam Antivirus (clamav) and ClamTK (GUI ClamAV) enables you to scan your computer and eliminate viruses/malware/ransomeware.""")
	os.system("sudo apt-get install clamav && sudo apt-get install clamtk")
	time.sleep(1)
	
	#KeePassXC is an oper-source, offline, and encrypted password manager
	print("""\nKeePassXC is an open-source, offline and encrypted password manager which allows you to save password securely.""")
	os.system("sudo apt-get install keepassxc")
	time.sleep(1)
	
	#GTKHash is a GUI hash checker
	print("""\nGTK Hash allows you to check hash fingerprinting of a file.""")
	os.system("sudo apt-get install gtkhash")
	time.sleep(1)
	
	print("-"*50)
	
	aClean()
	
	return()
	
def classicLin():

	print("Disabling Ubuntu Dock...\n")
	os.system("sudo apt-get purge gnome-shell-extension-ubuntu-dock")
	time.sleep()
	
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
	os.system("sudo snap remove snap-store")
	os.system("sudo snap remove gtk-common-themes")
	os.system("sudo snap remove gnome-3-34-1804
	os.system("sudo snap remove core18")
	os.system("sudo apt-get purge snapd")
	print("...")
	print("Done!\n")
	
	#as a substitution for a package manager, flatpak will be installed
	print("Installing Flatpak...\n")
	time.sleep(1)
	os.system("sudo apt-get install flatpak")
	os.system("flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo")
	os.system("sudo apt-get install gnome-software-plugin-flatpak")
	
	#install flatpak plugin installs snapd again so purging it again
	os.system("sudo apt-get purge gnome-software-plugin-snap")
	os.system("sudo apt-get purge snapd")
	print("...")
	print("Done!\n")
	
	time.sleep(1)
	#automatic updates are also a security risk
	print("Disabling automatic updates...\n")
	os.system("sudo apt-get purge update-notifier")
	
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
	os.system("sudo apt-get update")
	time.sleep(1)

	#running a full-upgrade to install upgrades and delete old packages
	print("-"*50)
	print("Upgrading")
	print("-"*50)
	os.system("sudo apt-get full-upgrade")
	time.sleep(1)
	
	#running the deSnapping program
	deSnap()
	
	return()
start_prog()
