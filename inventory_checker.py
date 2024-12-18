import yaml
from netmiko import ConnectHandler

# Load devices from YAML
with open('devices.yml') as f:
    data = yaml.safe_load(f)

compliant_devices = []
non_compliant_devices = []

for dev in data['devices']:
    conn = ConnectHandler(**dev)
    hostname = conn.send_command("show run | include hostname").split()[1]
    version = conn.send_command("show version | include Version")
    ntp_config = conn.send_command("show run | include ntp server")

    if "ntp server" in ntp_config:
        compliant_devices.append(hostname)
    else:
        non_compliant_devices.append(hostname)

    conn.disconnect()

print("=== Compliance Report ===")
print("Compliant devices:", compliant_devices)
print("Non-compliant devices:", non_compliant_devices)
