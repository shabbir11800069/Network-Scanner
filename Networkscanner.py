import socket

def scan_network(ip_range):
    for i in range(1,255):
        try:
            ip = ip_range + str(i)
            socket.inet_aton(ip)
            socket.gethostbyaddr(ip)
            print(ip, "is up")
        except socket.herror:
            print(ip, "is down or does not have a hostname")
        except socket.error:
            print(ip, "is invalid")

ip_range = "192.168.1."
scan_network(ip_range)
