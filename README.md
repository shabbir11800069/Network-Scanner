# Network-Scanner
This code uses a for loop to iterate through all IP addresses in the range of ip_range + 1 to 255. For each IP address, it uses the socket.inet_aton() method to check if the IP address is valid, and the socket.gethostbyaddr() method to check if the host is up.

If the host is up, the code prints the IP address and the message "is up". If the host is down or does not have a hostname, the code prints the IP address and the message "is down or does not have a hostname". If the IP address is invalid, it prints the message "is invalid".

The ip_range variable is set to "192.168.1." by default, but you can change it to any valid IP address range you want to scan.

Please keep in mind that this is a simple implementation and does not handle certain edge cases. It also does not have any feature to stop or limit the scan, so it will scan all 255 IP addresses in the provided range.
