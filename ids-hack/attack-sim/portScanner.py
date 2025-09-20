# save as simple_scanner.py
import socket

def is_port_open(host: str, port: int, timeout: float = 0.5) -> bool:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        s.close()
        return True
    except Exception:
        return False

if __name__ == "__main__":
    target = input("What is the target: ")        # <-- learning: keep to localhost or machines you own
    start_port, end_port = 1, 1024

    for p in range(start_port, end_port + 1):
        if is_port_open(target, p):
            print(f"Port {p} is open")