import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port, timeout=1):
    """
    Try to connect to a port on an IP. Return True if open, False otherwise.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            return result == 0
    except Exception:
        return False

def scan_ports(ip, start_port=1, end_port=1024, max_threads=100):
    """
    Scan ports in the given range on the specified IP.
    Returns a list of open ports.
    """
    open_ports = []

    def worker(port):
        if scan_port(ip, port):
            open_ports.append(port)

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(worker, range(start_port, end_port + 1))

    return sorted(open_ports)

if __name__ == "__main__":
    target = input("Enter IP or hostname to scan: ")
    start = int(input("Start port: "))
    end = int(input("End port: "))

    # Resolve hostname if needed
    try:
        ip_addr = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid hostname/IP")
        exit(1)

    print(f"Scanning {ip_addr} from port {start} to {end}...")
    open_ports = scan_ports(ip_addr, start, end)
    if open_ports:
        print("Open ports found:")
        for port in open_ports:
            print(f" - Port {port}")
    else:
        print("No open ports found.")
