import subprocess

print("MAC Changer")

interface = input("Enter interface name (e.g., eth0): ")
mac_addr = input("Enter new MAC address: ")

subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac_addr])
subprocess.call(["sudo", "ifconfig", interface, "up"])

print(f"MAC address for {interface} changed to {mac_addr}")
