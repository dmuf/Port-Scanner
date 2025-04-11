import socket
from termcolor import colored

def scan_ports(target, ports):
    print(f"Scanning {target}...\n")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(colored(f"Port {port} is OPEN", "green"))
        else:
            print(colored(f"Port {port} is CLOSED", "red"))
        sock.close()

# Example usage
target_ip = input("Enter IP to scan: ")
ports_to_scan = range(20, 1025)  # or [21, 22, 23, 80, 443] for custom
scan_ports(target_ip, ports_to_scan)

