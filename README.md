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

For the script itself, download 'PrivacyFocusedLinux.py'.

Thanks!
