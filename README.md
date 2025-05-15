# LFI-RFI-Plus
LFI &amp; RFI tool
Author : Shanmuk
# 🛡️ LFI-RFI Scanner Tool

A Python tool to scan for **Local File Inclusion (LFI)** and **Remote File Inclusion (RFI)** vulnerabilities.

## ✅ Features

- Tests against a list of common LFI/RFI payloads
- Detects responses containing sensitive content like `/etc/passwd` or PHP code
- Supports automation and scripting
- Saves vulnerable URLs to `vulnerabilities.txt`

## ⚙️ Requirements

- Python 3.x
- Internet connection
- Linux (Tested on Ubuntu/Kali)

Install `requests` module if needed:
```bash
pip3 install requests

Usage
➤ Option 1: Directly with Python

python3 scanner.py -u "http://example.com/index.php?page=FUZZ"

➤ Option 2: Using run.sh on Linux

chmod +x run.sh
./run.sh "http://example.com/index.php?page=FUZZ"
