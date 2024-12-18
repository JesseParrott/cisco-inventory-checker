# Cisco Inventory & Compliance Checker

This project provides an example Python script that:

- Connects to multiple Cisco devices (routers/switches).
- Retrieves basic inventory details (hostname, software version).
- Checks if the device is configured with an NTP server to ensure compliance.
- Outputs a compliance report directly in the terminal.

## Features

- Uses **Netmiko** for SSH connections.
- YAML file (`devices.yml`) to store device IPs and credentials.
- Easily customizable compliance checks (currently NTP servers).

## Prerequisites

- Python 3.x
- `pip install -r requirements.txt`
- Ensure devices are reachable from your environment.

## How to Run

1. Update `devices.yml` with your device details.
2. Run `python3 inventory_checker.py`.
3. Review the output in the terminal.
