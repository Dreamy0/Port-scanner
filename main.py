import sys
from socket import socket, AF_INET, SOCK_STREAM


def parse_range(parse: str) -> list:
    """
    Validates port range, returns start and stop of range in list. Format e.g <0-65535>

    start - value we want to start with
    stop - value we want to end with

    if - if we give wrong format it will print error warning
    return int(start), int(stop)- returning range in integer
    """
    start, stop = parse.split("-")

    if not start or not stop:
        print("Invalid format expected: 0-65535")

    return int(start), int(stop)


def scan_ports(ip: str, start: int, stop: int) -> int:
    """
    This function is responsible for checking if destination port is open or not

    loop for set range from start value to stop value + 1

    if result is equal to 0 port is open if not is closed
    """
    open_ports: int = 0
    print(f"Scanning ports {ip} from {start} to {stop}")
    for port in range(start, stop + 1):
        fd = socket(AF_INET, SOCK_STREAM)
        fd.settimeout(0.2)

        result = fd.connect_ex((ip, port))
        
        if result == 0:
            open_ports = open_ports + 1
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is close")

        fd.close()
    return open_ports


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("None arguments")
        sys.exit()

    ip = sys.argv[1]
    parse = sys.argv[2]

    if "-" not in parse:
        print("Invalid format expected: 0-65535")
        sys.exit()

    start, stop = parse_range(parse)
    scan_ports(ip, start, stop)
