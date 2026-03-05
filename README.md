Port Scanner using Python 

Checks common ports on a targetted host, python based code

basic network monitoring/reconnaissance 
script attempts to connect to the ports and reports back what ports open

Features:
-Scans the common used ports
-accepts domains and IP addresses
-Used python sockets to attempt connections
-displays the open ports after scanning

code to run: " py port_scanner.py <target>"
run in terminal vscode




example of output:

PS C:\Users\Local Admin\Desktop\CySe> py port_scanner.py google.com

Scan Target: 172.253.62.113
Scanning Ports..

Port 80 is Open
Port 443 is Open

Scan Complete.
PS C:\Users\Local Admin\Desktop\CySe> py port_scanner.py scanme.nmap.org

Scan Target: 45.33.32.156
Scanning Ports..

Port 22 is Open
Port 80 is Open

Scan Complete.
