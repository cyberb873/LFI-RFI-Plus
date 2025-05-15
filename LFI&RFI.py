import requests
import urllib.parse
import argparse
from datetime import datetime

def load_payloads():
    with open('payloads.txt', 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

def scan_url(url, payloads):
    vulnerable = []
    print(f"\n[+] Scanning URL: {url}")

    for payload in payloads:
        test_url = url.replace('FUZZ', urllib.parse.quote(payload))
        try:
            response = requests.get(test_url, timeout=5)
            if any(keyword in response.text.lower() for keyword in ['root:x:', 'localhost', '/bin/bash', '<?php']):
                print(f"[!] Potential vulnerability found: {test_url}")
                vulnerable.append(test_url)
        except requests.exceptions.RequestException:
            print(f"[-] Failed to connect: {test_url}")
    return vulnerable

def save_results(vuln_urls):
    if vuln_urls:
        with open('vulnerabilities.txt', 'w') as file:
            file.write(f"# Vulnerabilities Found - {datetime.now()}\n\n")
            for url in vuln_urls:
                file.write(url + '\n')
        print("\n[+] Results saved to vulnerabilities.txt")
    else:
        print("\n[-] No vulnerabilities found.")

def main():
    parser = argparse.ArgumentParser(description="LFI/RFI Scanner Tool")
    parser.add_argument("-u", "--url", help="Target URL with FUZZ param", required=True)
    args = parser.parse_args()

    if 'FUZZ' not in args.url:
        print("[!] Error: URL must contain the FUZZ keyword to inject payloads.")
        return

    payloads = load_payloads()
    vulnerabilities = scan_url(args.url, payloads)
    save_results(vulnerabilities)

if __name__ == "__main__":
    main()
