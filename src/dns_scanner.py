import asyncio
import time
import dns.resolver
from tqdm import tqdm
from src.session import get_session, save_session

async def check_dns(ip, timeout, domain):
    try:
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [ip]
        resolver.timeout = timeout
        resolver.lifetime = timeout

        start_time = time.time()
        answers = await asyncio.to_thread(resolver.resolve, domain, 'A')
        latency = (time.time() - start_time) * 1000  # in ms
        return ip, latency
    except Exception:
        return None, None


async def run_scan(ips, threads, timeout, domain, resume):
    if resume:
        session = get_session()
        good_dns = session.get("good_dns", [])
        scanned_ips = session.get("scanned_ips", set())
        ips_to_scan = [ip for ip in ips if ip not in scanned_ips]
    else:
        good_dns = []
        scanned_ips = set()
        ips_to_scan = ips

    pbar = tqdm(total=len(ips_to_scan), desc="Scanning DNS", unit="ip")

    semaphore = asyncio.Semaphore(threads)

    async def scan_ip(ip):
        async with semaphore:
            result_ip, latency = await check_dns(ip, timeout, domain)
            if result_ip:
                good_dns.append({"ip": result_ip, "latency": latency})
            scanned_ips.add(ip)
            pbar.update(1)
            if len(scanned_ips) % 100 == 0:
                save_session({"good_dns": good_dns, "scanned_ips": list(scanned_ips)})


    tasks = [scan_ip(ip) for ip in ips_to_scan]
    await asyncio.gather(*tasks)

    pbar.close()

    save_session({"good_dns": good_dns, "scanned_ips": list(scanned_ips)})
    return good_dns
