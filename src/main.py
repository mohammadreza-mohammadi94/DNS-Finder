import argparse
from src.config import TARGET_DOMAIN
from src.dns_scanner import run_scan
from src.utils import get_ips_from_file, get_ips_from_cidr
from src.reporter import save_report
import asyncio

def main():
    parser = argparse.ArgumentParser(description="DNS Finder - A multi-threaded DNS scanner.")
    parser.add_argument("-i", "--input", help="Input file with IPs or CIDR ranges (e.g., ips.txt or 1.1.1.1/24)", required=True)
    parser.add_argument("-o", "--output", help="Output file to save good DNS servers (e.g., good_dns.txt)", default="good_dns.txt")
    parser.add_argument("-t", "--threads", help="Number of threads to use for scanning", type=int, default=100)
    parser.add_argument("-T", "--timeout", help="DNS query timeout in seconds", type=float, default=1.0)
    parser.add_argument("-d", "--domain", help="Domain to test for resolution", default=TARGET_DOMAIN)
    parser.add_argument("-s", "--sample", help="Randomly sample a number of IPs from CIDR ranges", type=int)
    parser.add_argument("-r", "--resume", help="Resume a previous scan session", action="store_true")

    args = parser.parse_args()

    if "/" in args.input:
        ips = get_ips_from_cidr(args.input, args.sample)
    else:
        ips = get_ips_from_file(args.input)

    if not ips:
        print("No IPs to scan.")
        return

    good_dns = asyncio.run(run_scan(ips, args.threads, args.timeout, args.domain, args.resume))

    save_report(good_dns, args.output)

if __name__ == "__main__":
    main()
