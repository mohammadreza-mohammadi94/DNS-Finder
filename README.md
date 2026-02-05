# DNS Finder

A high-speed, asynchronous DNS scanner to find active and responsive DNS servers.

## Features

- **Multi-threaded & Asynchronous:** Utilizes `asyncio` for high-speed scanning of thousands of IPs.
- **Command-line Arguments:** Flexible control over input, output, threads, and timeout.
- **Real User Domain Test:** Verifies DNS resolvability using a real domain.
- **DNS Response Validation:** Ensures that the DNS server returns a valid A Record.
- **Latency Measurement:** Measures and records the response time of each DNS server.
- **Progress Bar:** Real-time progress tracking with `tqdm`.
- **Automatic Sorting:** Sorts the final list of DNS servers by latency.
- **Session Management:** Pause and resume long scans.
- **Random Sampling:** Scan a random subset of large IP ranges.
- **Cross-platform:** Works on both Windows and Linux.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/mohammadreza-mohammadi94/DNS-Finder.git
    cd DNS-Finder
    ```
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python -m src.main -i <input_file_or_cidr> -o <output_file> -t <threads> -T <timeout>
```

### Arguments

- `-i, --input`: Input file with IPs or CIDR ranges (e.g., `ips.txt` or `1.1.1.1/24`). (Required)
- `-o, --output`: Output file to save good DNS servers (e.g., `good_dns.txt`). (Default: `good_dns.txt`)
- `-t, --threads`: Number of concurrent tasks to use for scanning. (Default: 100)
- `-T, --timeout`: DNS query timeout in seconds. (Default: 1.0)
- `-d, --domain`: Domain to test for resolution. (Default: `example.com`)
- `-s, --sample`: Randomly sample a number of IPs from CIDR ranges.
- `-r, --resume`: Resume a previous scan session.

### Examples

- Scan IPs from a file:
  ```bash
  python -m src.main -i ips.txt -t 200
  ```
- Scan a CIDR range and save to a custom output file:
  ```bash
  python -m src.main -i 1.1.1.1/24 -o custom_dns.txt
  ```
- Scan a random sample of 1000 IPs from a large CIDR range:
  ```bash
  python -m src.main -i 8.8.8.8/16 -s 1000
  ```
- Resume a previous scan:
  ```bash
  python -m src.main -i ips.txt -r
  ```
