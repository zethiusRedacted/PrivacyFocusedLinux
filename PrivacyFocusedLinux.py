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
	 os.system("sudo apt-get -y autoremove --purge")
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
	
	#FireJail enables you to isolate your browser for safe browsing
	print("\nFirejail allows you to isolate an application, a browser or a file.")
	os.system("sudo apt-get install -y firejail")
	time.sleep(1)
	
	#AppArmor makes sure that apps do not uneccessary permissions
	print("\nAppArmor makes sure that applications do not have more permissions than is required of them.")
	os.system("sudo apt-get install -y apparmor-profiles apparmor-utils")
	#enabling these profiles
	time.sleep(1)
	print("\nEnabling profiles...")
	os.system("sudo aa-enforce /etc/apparmor.d/*")
	
	#Fail2ban makes sure SSH ports are not abused and spammed by malicious parties
	print("\nFail2ban prevents SSH port abuse by hackers.")
	os.system("sudo apt-get install -y fail2ban")
	#starting fail2ban generally and on every start up of the machine
	os.system("sudo systemctl enable fail2ban")
	os.system("sudo systemctl start fail2ban")
	#creating personal jail.local file to harden SSH
	os.system("""sudo echo "[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600" > /etc/fail2ban/jail.local""")
	
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
	
	#UFW or uncomplicated fire wall
	print("""\nUncomplicated Firewall blocks all shady traffic in or out of your computer.""")
	os.system("sudo apt-get install -y ufw")
	os.system("sudo ufw enable")
	print("Disabling incoming and forwarding traffic...")
	os.system("sudo ufw default deny incoming")
	os.system("sudo ufw default deny forward")
	time.sleep(1)
	#hardening UFW permissions to prevent SSH abuse
	os.system("sudo ufw limit 22/tcp")
	os.system("sudo ufw allow 80/tcp")
	os.system("sudo ufw allow 443/tcp")
	os.system("sudo ufw reload")

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
	
	time.sleep(1)
	#kernel-modules have been targetted by a recent malware
	#hence the user can disable them altogether
	#this is not recommended if you use nvidia drivers or virtualbox
	print("\nKernel Modules have been targetted recently by a malware designed for linux.")
	print("You can disable these modules completely.")
	print("Do you use Nvidia drivers or the application 'virtualbox'? (Y/N)")
	kern_mod = input()
	kern_mod.lower()
	
	if kern_mod == "n":
		os.system("sudo sysctl kernel.modules_disabled=1")
		os.system("sudo sysctl net.ipv4.conf.all.rp_filter")
	else:
		print("\nKernel Modules will remain untouched.")
	
	#many nmap scans have revealed the cups daemon to be a minor threat
	#it enables you to interface with printers
	#if you use a printer keeping this feature enabled is recommended
	print("""\nThe CUPS daemon helps you interface with printers if you use them. Would you like to disable the 'cups-daemon'? (Y/N)""")
	printer_question = input()
	printer_question.lower()
	
	if printer_question == "yes" or printer_question == "y":
		os.system("sudo apt-get purge -y cups-daemon")
	else:
		print("The 'cups-deamon' will remain untouched.")
	
	#denial of service attacks pose a massive threat on 'avahi-daemon'
	#'avahi-daemon' is only useful if you use apple products
	#if you use itunes or apple products, keeping this is recommended
	print("""\nThe AVAHI daemon helps you interface with apple products like 'iTunes'. If you use such features, would you like to disable 'avahi-deamon'? (Y/N)""")
	apple_question = input()
	apple_question.lower()
	
	if apple_question == "yes" or apple_question == "y":
		os.system("sudo apt-get purge -y avahi-daemon")
	else:
		print("The 'avahi-daemon' will remain untouched.")
	
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
		
	#removing all the reporting packages after the previous step disabled them
	print("Disabling and purging reporting packages...\n")
	time.sleep(1)
	os.system("sudo apt-get purge -y ubuntu-report popularity-contest apport apport-symptoms whoopsie")
	print("Holding removed privacy and security risking packages...\n")
	time.sleep(1)
	os.system("sudo apt-mark hold avahi-daemon snapd cups-daemon update-notifier gnome-shell-extension-ubuntu-dock gnome-shell-extension-desktop-icons ubuntu-report popularity-contest apport apport-symptoms whoopsie")
	print("...")
	print("Done!\n")
	
	#hardening network configuration
	print("Hardening network config files...\n")
	time.sleep(1)
	os.system("sudo sed -i 's/#net.ipv4.conf.default.rp_filter=1/net.ipv4.conf.default.rp_filter=1/g' /etc/sysctl.conf")
	os.system("sudo sed -i 's/#net.ipv4.conf.all.rp_filter=1/net.ipv4.conf.all.rp_filter=1/g' /etc/sysctl.conf")
	os.system("sudo sed -i 's/#net.ipv4.conf.all.accept_redirects\ \=\ \0/net.ipv4.conf.all.accept_redirects=0/g' /etc/sysctl.conf")
	os.system("sudo sed -i 's/#net.ipv6.conf.all.accept_redirects\ \=\ \0/net.ipv6.conf.all.accept_redirects=0/g' /etc/sysctl.conf")
	os.system("sudo sed -i 's/#net.ipv4.conf.all.send_redirects\ \=\ \0/net.ipv4.conf.all.send_redirects=0/g' /etc/sysctl.conf")
	os.system("sudo sed -i 's/#net.ipv4.conf.all.accept_source_route\ \=\ \0/net.ipv4.conf.all.accept_source_route=0/g' /etc/sysctl.conf")
	os.system("sudo sed -i 's/#net.ipv6.conf.all.accept_source_route\ \=\ \0/net.ipv6.conf.all.accept_source_route=0/g' /etc/sysctl.conf")
	os.system("sudo sed -i 's/#net.ipv4.conf.all.log_martians\ \=\ \1/net.ipv4.conf.all.log_martians=1/g' /etc/sysctl.conf")
	print("...")
	print("Done!\n")
	
	
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
