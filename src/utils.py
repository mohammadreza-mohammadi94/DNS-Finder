import ipaddress
import random

def get_ips_from_file(file_path):
    try:
        with open(file_path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: Input file not found at {file_path}")
        return []

def get_ips_from_cidr(cidr_range, sample_size=None):
    try:
        network = ipaddress.ip_network(cidr_range, strict=False)
        ips = [str(ip) for ip in network.hosts()]
        if sample_size and sample_size < len(ips):
            return random.sample(ips, sample_size)
        return ips
    except ValueError:
        print(f"Error: Invalid CIDR range: {cidr_range}")
        return []
