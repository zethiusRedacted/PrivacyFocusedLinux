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
- 'avahi-daemon' and 'cups-daemon' can be removed as they pose a security and a privacy threat. [1]
- The firewall (UFW) is enabled to disable all incoming and forwarding traffic. [1]
- AppArmour profiles are installed and enabled so apps do not have more than required permissions. [1]

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
- AppArmor profiles and utils for better and more enhanced profiles so apps do not have more than required permissions.[1]
- Firefail to isolate browsers and applications for a safe browsing environment. [1]

In addition to these tools, I would recommend installing some others.
- Signal Desktop for an open source messaging procedure which is end to end encrypted.
- BleachBit for maintenance.
- VeraCrypt for document and drive encryption.

For the script itself, look at 'PrivacyFocusedLinux.py'.

Thanks!

--------------------------------------------------
Update: 29th June, 2020 - Update [1]

- [PRIVACY RISK] cups-daemon: CUPS daemon is a service used by applications to interface with printers. This script now gives you a choice to remove CUPS service altogether if you do not use printers. NMAP scans can gather information from CUPS service which pose a minor security threat. So, if you do not use a printer, you can let the script do so. User gets a choice to disable, remove or leave the service untouched.
- [PRIVACY RISK] avahi-daemon: The daemon registers local IP addresses and static services using mDNS/DNS-SD. A 'denial of service' vulnerability was exposed in this daemon. So, if you do not interact with Apple Products on your computer, this daemon can be completely removed, disabled or can remain untouched.
- [SECURITY RISK] UFW is now programmed to disable all forwarding traffic too.
- [PRIVACY AND SECURITY RISK] AppArmor Profiles: App armour now lets you install more profiles so the applications you have installed do not do more than they are supposed to.
- [PRIVACY UTILITY] Firejail: Firejail is installed so you can isolate applications like your browser for unsafe browsing, etc.
--------------------------------------------------
Update: 25th August, 2020 - Update [2]

News: A new malware was released for linux kernel modules. This update will ensure you do not get affected by it.

- [Security Risk] fail2ban: fail2ban is installed and is auto-started for the user. Fail2ban prevents hacking by SSH which is the most common types of attacks. A local jail is created for the user focused on SSH hacking.
- [Security Risk] UFW permissions: UFW permissions are altered to focus on SSH hacking and preventing spamming by an attacker.
- [Security Risk] Kernel Modules: Since this new malware is in the form of a kernel module, the user is given a choice of disabling them completely if they do not use apps such as virtual box or have no Nividia drivers installed.
--------------------------------------------------
