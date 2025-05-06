import json

def parse_dnsmasq_config(file_path):
    entries = []

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('address=') and '/' in line:
                try:
                    _, rest = line.split('=', 1)
                    parts = rest.split('/')
                    if len(parts) == 3:
                        _, domain, ip = parts
                        entry = {
                            "type": "a",
                            "name": domain,
                            "value": ip
                        }
                        entries.append(entry)
                except ValueError:
                    continue  # Skip malformed lines

    return entries

def write_json(entries, output_path):
    with open(output_path, 'w') as f:
        json.dump(entries, f, indent=3)

# Example usage
if __name__ == "__main__":
    config_path = 'dnsmasq.conf'  # Input file path
    output_path = 'dns_zones.json'  # Output JSON path
    entries = parse_dnsmasq_config(config_path)
    write_json(entries, output_path)
