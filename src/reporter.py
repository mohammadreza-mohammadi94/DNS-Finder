def save_report(good_dns, output_file):
    if not good_dns:
        print("No good DNS servers found.")
        return

    # Sort by latency
    sorted_dns = sorted(good_dns, key=lambda x: x['latency'])

    with open(output_file, "w") as f:
        for dns in sorted_dns:
            f.write(f"{dns['ip']} - {dns['latency']:.2f}ms\n")

    print(f"Scan complete. Found {len(sorted_dns)} good DNS servers.")
    print(f"Results saved to {output_file}")

