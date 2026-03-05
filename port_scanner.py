import socket
import sys

def scan_ports(target, ports):
    print(f"\nScan Target: {target}")
    print("Scanning Ports..\n")

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"Port {port} is Open")

            sock.close()

        except KeyboardInterrupt:
            print("\nScan Stopped")
            sys.exit()

        except socket.gaierror:
            print("Hostname Encountered Error")
            sys.exit()

        except socket.error:
            print("Server Failed")
            sys.exit()

    print("\nScan Complete.")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python port_scanner.py <target>")
        sys.exit()

    target = socket.gethostbyname(sys.argv[1])  

    common_ports = [
        21,
        22,
        23,
        25,
        53,
        80,
        110,
        139,
        143,
        443,
        445,
        3389
    ]

    scan_ports(target, common_ports)